from django.urls import path

from FreiRui.views.pictures.edit import image_edit

urlpatterns = [
    path('picture/<path:picture_path>/edit/', image_edit, name='image_edit'),
]
