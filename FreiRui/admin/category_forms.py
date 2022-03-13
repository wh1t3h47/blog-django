from django import forms
from ..models.Categories import Categories


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ('name', 'published', 'listing_type',
                  'order', 'short_name', 'title', 'video_url')
