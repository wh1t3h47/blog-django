from django.db import models
from django.template.defaultfilters import slugify
from random import randint
from .Gallery import Gallery


def get_image_filename(instance, filename):
    # title = instance.post.title
    # slug = slugify(title)
    name = filename[:-4]
    extension = filename[-3:]
    number = randint(1, 10000)
    return f"images/{name}-{number}.{extension}"


class Images(models.Model):
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
