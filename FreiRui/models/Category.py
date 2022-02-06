from typing import Literal, Union
from django.db import models

CATEGORY_LENGTH = 30


class Category(models.Model):
    ''' A category is a group of posts that will be avaliable in the navbar '''
    name = models.CharField(max_length=CATEGORY_LENGTH, verbose_name="Nome (barra de ferramentas)")
    short_name = models.CharField(max_length=CATEGORY_LENGTH, verbose_name="Nome curto (singular)")
    title = models.CharField(max_length=255, verbose_name="Título (página)")
    listing_type: Union[Literal['accordion'], Literal['cards'], Literal['single']
                        ] = models.CharField(max_length=10, default="cards")
    published = models.BooleanField()
    ''' Boolean, if not published, will hide the category from the menu. '''
    order = models.IntegerField(default=0, verbose_name="Ordem da categoria na listagem")

    def __str__(self) -> str:
        return self.name

    def __bool__(self) -> bool:
        return self.published
