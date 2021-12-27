from django.db import models

CATEGORY_LENGTH = 30


class Category(models.Model):
    ''' A category is a group of posts that will be avaliable in the navbar '''
    name = models.CharField(max_length=CATEGORY_LENGTH)
    published = models.BooleanField()
    ''' Boolean, if not published, will hide the category from the menu. '''

    def __str__(self):
        return self.name

    def __bool__(self):
        return self.published
