from django.conf import settings
from django.db import models
from django.utils import timezone

from FreiRui.models.Galleries import Galleries
from .Categories import Categories, CATEGORY_LENGTH

TITLE_LENGTH = 200


class Posts(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Categories, on_delete=models.DO_NOTHING,
        verbose_name="Categoria da postagem", db_index=True)
    title = models.CharField(max_length=TITLE_LENGTH,
                             verbose_name="Título", blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True,
        verbose_name="Data de publicação (selecione no futuro para agendar)",
        db_index=True)
    galleries = models.ManyToManyField(Galleries, blank=True)
    is_deleted = models.BooleanField(default=False, verbose_name="Ocultado?",
                                     db_index=True)
    instagram_posted = models.BooleanField(default=False)
    facebook_posted = models.BooleanField(default=False)

    def publish(self):
        # self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
