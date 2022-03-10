from django.db import models


class Galleries(models.Model):
    '''
    A Galleries is used to group images together and has relation to a post,
    the reason for that is so we can upload the images without having to
    create a post first, but we can still group them.
    '''
    # Categories
