from django import forms
from ..models.Category import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'published', 'listing_type', )
