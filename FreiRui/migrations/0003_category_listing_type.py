# Generated by Django 3.2.10 on 2022-02-01 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FreiRui', '0002_post_galleries'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='listing_type',
            field=models.CharField(default='cards', max_length=10),
        ),
    ]
