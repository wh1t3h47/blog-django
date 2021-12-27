from django.urls import path

from FreiRui.views.gallery.new import gallery_new

urlpatterns = [
    path('gallery/new/', gallery_new, name='gallery_new'),
]
