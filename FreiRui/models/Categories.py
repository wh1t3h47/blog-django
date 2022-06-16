from typing import Literal, Union
from django.db import models

CATEGORY_LENGTH = 30


class Categories(models.Model):
    ''' A category is a group of posts that will be avaliable in the navbar '''
    name = models.CharField(max_length=60, unique=True,
                            verbose_name="Nome (barra de ferramentas)",
                            db_index=True)
    short_name = models.CharField(
        max_length=CATEGORY_LENGTH, verbose_name="Nome curto (singular)",
        blank=True)
    title = models.CharField(
        max_length=255,
        verbose_name="Título (página)",
        blank=True)
    listing_type: Union[Literal['accordion'],
                        Literal['cards'],
                        Literal['single'],
                        Literal['youtube']
                        ] = models.CharField(max_length=10, default="cards")
    published = models.BooleanField(
        verbose_name="Publicado", default=True, db_index=True)
    ''' Boolean, if not published, will hide the category from the menu. '''
    order = models.IntegerField(
        default=0, verbose_name="Ordem da categoria na listagem",
        db_index=True)
    video_url = models.CharField(
        max_length=255, blank=True, null=True,
        verbose_name="ID do canal do YouTube")

    def __str__(self) -> str:
        return self.name

    def __bool__(self) -> bool:
        return self.published
