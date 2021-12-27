from django.urls import path

from . import category, post, gallery

urlpatterns = category.urlpatterns + post.urlpatterns + gallery.urlpatterns
