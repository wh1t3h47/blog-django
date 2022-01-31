from django.urls import path

from FreiRui.views.gallery.new import gallery_new
from FreiRui.views.gallery.list import gallery_list

urlpatterns = [
    path('gallery/new/', gallery_new, name='gallery_new'),
    path('gallery/list/', gallery_list, name='gallery_list'),
]
