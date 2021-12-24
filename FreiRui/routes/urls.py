from django.urls import path

from ..views.post.list import post_list
from ..views.post.details import post_details
from ..views.post.new import post_new
from ..views.post.edit import post_edit

urlpatterns = [
    path('posts', post_list, name='post_list'),
    path('post/<int:pk>/', post_details, name='post_details'),
    path('post/new/', post_new, name='post_new'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    # multi file upload
]
