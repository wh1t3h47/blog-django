from django import forms
from ..models.Category import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'published', 'listing_type', 'order', 'short_name', 'title', 'video_url')
