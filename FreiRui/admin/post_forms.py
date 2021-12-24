from django import forms
from ..models.Post import Post
from .image_form import ImageForm


class FileFieldForm(forms.Form):
    file_field = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}))


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'published_date',)
