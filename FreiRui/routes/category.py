from django.urls import path

from FreiRui.views.category.new import category_new
from FreiRui.views.category.edit import category_edit

urlpatterns = [
    path('category/<int:pk>/edit/', category_edit, name='category_edit'),
    path('category/new/', category_new, name='category_new'),
]
