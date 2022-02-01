from django import forms
from ..models.Images import Images


class EditImageForm(forms.ModelForm):
    images = forms.FileField(label=False, required=True,
                             widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Images
        fields = ('images', )
