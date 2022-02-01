from django.db import models
from random import randint

from .Gallery import Gallery


def get_image_filename(instance, filename: str):
    if instance.edit_image:
        # Nesse caso estamos editando a imagem e queremos conservar o
        # nome original
        return instance.image_url
    # title = instance.post.title
    # slug = slugify(title)
    name = filename[:-4]
    extension = filename[-3:]
    number = randint(0, 1000000)
    return f"images/{name}-{number}.{extension}"


class Images(models.Model):
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Images')
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
