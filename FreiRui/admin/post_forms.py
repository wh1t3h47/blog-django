from django import forms
from FreiRui.models.Posts import Posts

# class FileFieldForm(forms.Form):
#     file_field = forms.FileField(
#         widget=forms.ClearableFileInput(attrs={'multiple': True}))


class PostForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ('title', 'text', 'published_date',
                  'category', 'galleries', 'is_deleted', )
