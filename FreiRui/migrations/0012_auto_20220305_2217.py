# Generated by Django 3.2.10 on 2022-03-05 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FreiRui', '0011_category_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='short_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='Nome curto (singular)'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='video_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ID do canal do YouTube'),
        ),
    ]
