# Generated by Django 3.2.10 on 2022-03-05 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FreiRui', '0010_auto_20220206_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='video_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='URL do vídeo'),
        ),
    ]