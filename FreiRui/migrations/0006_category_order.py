# Generated by Django 3.2.10 on 2022-02-02 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FreiRui', '0005_alter_post_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]