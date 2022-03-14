from django.urls import path

from FreiRui.views.post.list import post_list
from FreiRui.views.post.details import post_details
from FreiRui.views.post.new import post_new
from FreiRui.views.post.edit import post_edit

urlpatterns = [
    path('postagens/<str:category>/', post_list, name='post_list'),
    path('postagens/<str:category>/<int:pk>/',
         post_details, name='post_details'),
    path('postagem/criar/<str:category>', post_new, name='post_new'),
    path('postagens/<int:pk>/editar/', post_edit, name='post_edit'),
]
