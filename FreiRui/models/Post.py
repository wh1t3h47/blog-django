from django.conf import settings
from django.db import models
from django.utils import timezone

from FreiRui.models.Gallery import Gallery
from .Category import Category, CATEGORY_LENGTH

TITLE_LENGTH = 200


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # category = models.CharField(max_length=CATEGORY_LENGTH, choices=Category.objects.filter(published=True, ).order_by('order'))
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, verbose_name="Categoria da postagem")
    title = models.CharField(max_length=TITLE_LENGTH, verbose_name="Título")
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True, verbose_name="Data de publicação (selecione no futuro para agendar)")
    galleries = models.ManyToManyField(Gallery, blank=True)
    is_deleted = models.BooleanField(default=False, verbose_name="Ocultado?")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
