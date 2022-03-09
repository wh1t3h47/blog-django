from django.urls import path

from FreiRui.views.index import index

urlpatterns = [
    path('', index, name='index'),
]
