from typing import Union
from django import forms
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from FreiRui.models.Images import Images
from FreiRui.admin.post_forms import PostForm
from FreiRui.admin.image_forms import ImageForm
from FreiRui.models.Post import Post

ResponseOrRedirect = Union[HttpResponseRedirect, HttpResponse]


@login_required
def post_edit(request: HttpRequest, pk: str) -> ResponseOrRedirect:
    def return_rendered_html(post_form: PostForm) -> HttpResponse:
        post = get_object_or_404(Post, pk=pk)
        post_form.fields['title'].widget.attrs['value'] = post.title
        post_form.fields['text'].widget.attrs['value'] = post.text
        post_form.fields['text'].widget = forms.HiddenInput()
        post_form.fields['published_date'].widget.attrs['value'] = post.published_date
        post_form.fields['published_date'].widget.attrs['autocomplete'] = "off"
        post_form.fields['category'].widget.attrs['value'] = post.category
        default_values = {
            'title': post.title,
            'text': post.text,
            'published_date': post.published_date,
            'category': post.category
        }
        # print(f'formset: {formset}')
        return render(request, 'post/edit.html',
                      {'post_form': post_form, 'default_values': default_values})

    if request.method == "POST":
        post = get_object_or_404(Post, pk=pk)
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form = post_form.save(commit=False)
            post_form.user = request.user
            post_form.published_date = timezone.now()
            post_form.save()
            return HttpResponseRedirect(f"/post/{pk}")
        else:
            print(post_form.errors)
    # print(f'formset: {formset}')
        return return_rendered_html(post_form)

    # else if request.method == "GET":
    post_form = PostForm()
    return return_rendered_html(post_form)
