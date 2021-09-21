"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import blog.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.main, name='main'),
    path('detail/<str:id>/', blog.views.detail, name='detail'),
    path('write/', blog.views.write, name='write'),
    path('write/create/', blog.views.create, name='create'),
    path('base/', blog.views.base, name='base'),
    path('edit/<str:id>/', blog.views.edit, name='edit'),
    path('delete/<str:id>/', blog.views.delete, name='delete'),
    path('hashtag/', blog.views.hashtagform, name='hashtag'),
    path('<int:hashtag_id>/search/', blog.views.search, name='search'),
    path('account/', include('account.urls')),
    path('calendar/', blog.views.calendar_view, name="calendar"),#일정
    path('event/new/', blog.views.event, name="new"),#일정 생성
    path('event/edit/<int:event_id>', blog.views.event, name="edit"),#일정 수정
    path('commu_like/<int:pk>', blog.views.commu_like, name='commu_like'),
    path('bookmark/', include('bookmark.urls')),#북마크앱 url
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
