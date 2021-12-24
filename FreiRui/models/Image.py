from django.db import models
from django.template.defaultfilters import slugify
from .Post import Post


def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return f"images/{slug}-{filename}"


class Images(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')
