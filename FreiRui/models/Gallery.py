from django.db import models
from .Post import Post


class Gallery(models.Model):
    '''
    A gallery is used to group images together and has relation to a post,
    the reason for that is so we can upload the images without having to
    create a post first, but we can still group them.
    '''
    post = models.ForeignKey(
        Post, default=None, on_delete=models.CASCADE, blank=True, null=True)
    '''
    A gallery has to belong to a post, but we set default to None, the
    reason for that is so we can upload the images without having to
    create a post first, but we can still group them.
    '''
