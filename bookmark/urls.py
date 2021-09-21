from django.urls import path
import bookmark.views
from .views import *
urlpatterns = [
    path('', bookmark.views.bookmark_category, name='bookmark_category'),
    path('<int:book_category_id>/bookmark_list/', bookmark.views.bookmark_list, name='bookmark_list'),
    path('bookmark_update/<int:pk>/', BookmarkUpdate.as_view(), name='bookmark_update'),
    path('bookmark_delete/<int:pk>/', BookmarkDelete.as_view(), name='bookmark_delete'),
    path('bookmark_create/', BookmarkCreate.as_view(), name='bookmark_create'),
    path('bookmark_detail/<int:pk>/', BookmarkDetail.as_view(), name='bookmark_detail'),
]
