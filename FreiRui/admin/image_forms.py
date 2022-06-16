from django import forms
from FreiRui.models.Images import Images


class ImageForm(forms.ModelForm):
    images = forms.FileField(label="Imagens", required=True,
                             widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Images
        fields = ('images', )
