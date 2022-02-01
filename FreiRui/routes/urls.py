from django.urls import path

from . import category, post, gallery, picture

urlpatterns = category.urlpatterns + post.urlpatterns + \
    gallery.urlpatterns + picture.urlpatterns
