from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog, Hashtag, Event
from .forms import CreateForm, CommentForm, HashtagForm, EventForm
import datetime #다이어리용
import calendar#다이어리용
from .calendar import Calendar #다이어리용
from django.utils.safestring import mark_safe #다이어리용
from django.http.response import HttpResponse#좋아요용

# Create your views here.

def main(request):
    blogs = Blog.objects
    hashtags = Hashtag.objects
    return render(request, 'blog/main.html', {'blogs':blogs, 'hashtags':hashtags})

def write(request):
    return render(request, 'blog/write.html')

#왤까... 이게 된 이유가... 이게 원래꺼(m2m 안됐던거임)
# def create(request, blog=None):
#    if request.method == "POST":
#       form = CreateForm(request.POST, instance=blog)
#        if form.is_valid():
#            blog = form.save(commit=False)
#            form.save_m2m()
#            blog.pub_date = timezone.datetime.now()
#            blog.save()
#            return redirect('main')
#    else:
#        form = CreateForm(instance=blog)
#        return render(request, 'blog/write.html', {'form':form})

#def blogform(request, blog=None):
#    if request.method == 'POST':
#        form = CreateForm(request.POST, instance=blog)
#        if form.is_valid():
#            blog = form.save(commit=False)
#            blog.pub_date = timezone.datetime.now()
#            blog.save()
#            form.save_m2m()
#            return redirect('main')
#    else:
#        form = CreateForm(instance=blog)
#        return render(request, 'blog/write.html', {'form':form})

def create(request, blog=None):
    if request.method == "POST":
        form = CreateForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.pub_date = timezone.datetime.now()
            blog.save()
            form.save_m2m()
            return redirect('main')
    else:
        form = CreateForm(instance=blog)
        return render(request, 'blog/write.html', {'form':form})


def blogform(request, blog=None):
    if request.method == 'POST':
        form = CreateForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.pub_date = timezone.datetime.now()
            blog.save()
            form.save_m2m()
            return redirect('main')
    else:
        form = CreateForm(instance=blog)
        return render(request, 'blog/write.html', {'form':form})

def base(request):
    return render(request, 'blog/base.html')

def edit(request, id):
    blog = get_object_or_404(Blog, id = id)
    if request.method == "POST":
        form = CreateForm(request.POST, instance=blog)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('main')
    else:
        form = CreateForm(instance=blog)
    return render(request, 'blog/edit.html', {'form':form})

def delete(request, id):
    delete_blog = get_object_or_404(Blog, id = id)
    delete_blog.delete()
    return redirect ('main')

# 디테일
def detail(request, id):
    blog = get_object_or_404(Blog, id = id)
    default_view_count = blog.view_count
    blog.view_count = default_view_count + 1
    blog.save()
    return render(request, 'blog/detail.html', {'blog':blog})

# 해시태그 함수
def hashtagform(request, hashtag=None):
    if request.method == 'POST':
        form = HashtagForm(request.POST, instance=hashtag)
        if form.is_valid():
            hashtag = form.save(commit=False)
            if Hashtag.objects.filter(name=form.cleaned_data['name']):
                form = HashtagForm()
                error_message = "이미 존재하는 해시태그 입니다."
                return render(request, 'blog/hashtag.html', {'form':form, "error_message": error_message})
            else:
                hashtag.name = form.cleaned_data['name']
                hashtag.save()
            return redirect('main')
    else:
        form = HashtagForm(instance=hashtag)
        return render(request, 'blog/hashtag.html', {'form':form})

def search(request, hashtag_id):
    hashtag = get_object_or_404(Hashtag, id=hashtag_id)
    return render(request, 'blog/search.html', {'hashtag':hashtag})

#다이어리 페이지
def calendar_view(request):
    today = get_date(request.GET.get('month'))

    prev_month_var = prev_month(today)
    next_month_var = next_month(today)

    cal = Calendar(today.year, today.month)
    html_cal = cal.formatmonth(withyear=True)
    result_cal = mark_safe(html_cal)

    context = {'calendar' : result_cal, 'prev_month' : prev_month_var, 'next_month' : next_month_var}

    return render(request, 'blog/diary_events.html', context)

#현재 달력을 보고 있는 시점의 시간을 반환
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime.date(year, month, day=1)
    return datetime.datetime.today()

#현재 달력의 이전 달 URL 반환
def prev_month(day):
    first = day.replace(day=1)
    prev_month = first - datetime.timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

#현재 달력의 다음 달 URL 반환
def next_month(day):
    days_in_month = calendar.monthrange(day.year, day.month)[1]
    last = day.replace(day=days_in_month)
    next_month = last + datetime.timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

#새로운 Event의 등록 혹은 수정
def event(request, event_id=None):
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return redirect('calendar')
    return render(request, 'blog/diary_input.html', {'form': form})

#좋아요
def commu_like(request, pk):
    if not request.user.is_active:
        return HttpResponse('First SignIn please')

    blog = get_object_or_404(Blog, pk=pk)
    user = request.user

    if blog.Blog_likes.filter(id=user.id).exists():
        blog.Blog_likes.remove(user)
    else:
        blog.Blog_likes.add(user)
    
    return redirect('detail', pk)