from typing import List
from django import forms
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from FreiRui.admin.post_forms import PostForm
from FreiRui.models.Categories import Categories
from FreiRui.models.Posts import Posts
from FreiRui.views.category.get_categories import get_categories


def return_rendered_html_forms(request: HttpRequest, post_form: PostForm, pk: str = None, category: str = '') -> HttpResponse:
    post: Posts = None
    if pk:
        post = get_object_or_404(Posts, pk=pk)
    if post:
        post_form.fields['title'].widget.attrs['value'] = post.title
        post_form.fields['text'].widget.attrs['value'] = post.text
        post_form.fields['published_date'].widget.attrs['value'] = post.published_date
        post_form.fields['is_deleted'].widget.attrs['checked'] = post.is_deleted
    post_form.fields['text'].widget.attrs['required'] = True
    post_form.fields['text'].widget = forms.HiddenInput()
    post_form.fields['published_date'].widget.attrs['autocomplete'] = "off"
    post_form.fields['published_date'].widget.attrs['required'] = True
    post_form.fields['galleries'].widget.attrs['style'] = "display: none;"

    default_values = {}
    if post:
        default_values = {
            'title': post.title,
            'text': post.text,
            'published_date': post.published_date,
            'category': post.category,
            'galleries': [str(x) for x in [*post.galleries.all()]]
        }
    if category:
        default_values['category'] = category
    # print(f'formset: {formset}')
    categories = get_categories(request)
    return render(request, 'post/edit.html',
                  {'post_form': post_form, 'default_values': default_values, 'categories': categories})
