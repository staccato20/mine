from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100, default='누구신지?')
    pub_date = models.DateTimeField('date published')
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    hashtags = models.ManyToManyField('Hashtag', blank=True)
    Blog_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="Blog_likes")
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
        
#댓글
class Comment(models.Model):
    def __str__(self):
        return self.text

    post_id = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=50)

#해시태그
class Hashtag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

#스크랩
class Bookmark(models.Model):
    book_site_name = models.CharField(max_length=50)
    book_url = models.URLField()
    
    def __str__(self):
        return self.book_site_name + " : " + self.book_url

    class Meta:
        ordering = ["book_site_name"]

# 다이어리
class Event(models.Model):
    diary_start_time = models.DateTimeField("시작시간")
    diary_end_time = models.DateTimeField("마감시간")
    diary_title = models.CharField("이벤트 이름", max_length=50)
    diary_description = models.TextField("상세")

    class Meta:
        verbose_name = "이벤트 데이터"
        verbose_name_plural = "이벤트 데이터"

    def __str__(self):
        return self.diary_title

    @property
    def get_html_url(self):
        diary_url = reverse('edit', args=(self.id,))
        return f'<a href="{diary_url}"> {self.diary_title} </a>'