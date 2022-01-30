from django import forms
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from FreiRui.admin.post_forms import PostForm
from FreiRui.models.Post import Post


def return_rendered_html_forms(request: HttpRequest, post_form: PostForm, pk: str = None) -> HttpResponse:
        post: Post = None
        if pk:
            post = get_object_or_404(Post, pk=pk)
        if post:
            post_form.fields['title'].widget.attrs['value'] = post.title
            post_form.fields['text'].widget.attrs['value'] = post.text
            post_form.fields['published_date'].widget.attrs['value'] = post.published_date
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
        # print(f'formset: {formset}')
        return render(request, 'post/edit.html',
                      {'post_form': post_form, 'default_values': default_values})