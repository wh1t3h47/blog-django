from django.urls import path

from FreiRui.views.gallery.new import gallery_new
from FreiRui.views.gallery.list import gallery_list

urlpatterns = [
    path('Galleries/new/', gallery_new, name='gallery_new'),
    path('Galleries/list/', gallery_list, name='gallery_list'),
]
