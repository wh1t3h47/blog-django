from django import forms
from ..models.Image import Images


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image', required=False)

    class Meta:
        model = Images
        fields = ('image', )
