from django.urls import path
from .views import *

urlpatterns = [
    path('', PostsView.as_view(), name='posts_list_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetailView.as_view(), name='post_detail_url'),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete_url'),
    path('tags/', TagList.as_view(), name='tags_list_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetailView.as_view(), name='tag_detail_url'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<str:slug>/delete/', tagDelete, name='tag_delete_url')

]
