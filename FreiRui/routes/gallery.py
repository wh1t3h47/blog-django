from django.urls import path

from FreiRui.views.gallery.new import gallery_new
from FreiRui.views.gallery.list import gallery_list

urlpatterns = [
    path('galleries/new/', gallery_new, name='gallery_new'),
    path('galleries/list/', gallery_list, name='gallery_list'),
]
