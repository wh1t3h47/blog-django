from typing import Literal, Union
from django.db import models

CATEGORY_LENGTH = 30


class Category(models.Model):
    ''' A category is a group of posts that will be avaliable in the navbar '''
    name = models.CharField(max_length=CATEGORY_LENGTH)
    listing_type: Union[Literal['accordion'], Literal['cards']
                        ] = models.CharField(max_length=10, default="cards")
    published = models.BooleanField()
    ''' Boolean, if not published, will hide the category from the menu. '''

    def __str__(self) -> str:
        return self.name

    def __bool__(self) -> bool:
        return self.published
