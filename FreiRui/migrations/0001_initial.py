# Generated by Django 4.0.3 on 2022-06-16 02:18

import FreiRui.models.Images
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=60, unique=True, verbose_name='Nome (barra de ferramentas)')),
                ('name_de', models.CharField(db_index=True, max_length=60, null=True, unique=True, verbose_name='Nome (barra de ferramentas)')),
                ('name_en', models.CharField(db_index=True, max_length=60, null=True, unique=True, verbose_name='Nome (barra de ferramentas)')),
                ('name_pt', models.CharField(db_index=True, max_length=60, null=True, unique=True, verbose_name='Nome (barra de ferramentas)')),
                ('short_name', models.CharField(blank=True, max_length=30, verbose_name='Nome curto (singular)')),
                ('short_name_de', models.CharField(blank=True, max_length=30, null=True, verbose_name='Nome curto (singular)')),
                ('short_name_en', models.CharField(blank=True, max_length=30, null=True, verbose_name='Nome curto (singular)')),
                ('short_name_pt', models.CharField(blank=True, max_length=30, null=True, verbose_name='Nome curto (singular)')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Título (página)')),
                ('title_de', models.CharField(blank=True, max_length=255, null=True, verbose_name='Título (página)')),
                ('title_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Título (página)')),
                ('title_pt', models.CharField(blank=True, max_length=255, null=True, verbose_name='Título (página)')),
                ('listing_type', models.CharField(default='cards', max_length=10)),
                ('published', models.BooleanField(db_index=True, default=True, verbose_name='Publicado')),
                ('published_de', models.BooleanField(db_index=True, default=True, verbose_name='Publicado')),
                ('published_en', models.BooleanField(db_index=True, default=True, verbose_name='Publicado')),
                ('published_pt', models.BooleanField(db_index=True, default=True, verbose_name='Publicado')),
                ('order', models.IntegerField(db_index=True, default=0, verbose_name='Ordem da categoria na listagem')),
                ('video_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='ID do canal do YouTube')),
                ('video_url_de', models.CharField(blank=True, max_length=255, null=True, verbose_name='ID do canal do YouTube')),
                ('video_url_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='ID do canal do YouTube')),
                ('video_url_pt', models.CharField(blank=True, max_length=255, null=True, verbose_name='ID do canal do YouTube')),
            ],
        ),
        migrations.CreateModel(
            name='Galleries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('title_de', models.CharField(max_length=200, null=True, verbose_name='Título')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Título')),
                ('title_pt', models.CharField(max_length=200, null=True, verbose_name='Título')),
                ('text', models.TextField()),
                ('text_de', models.TextField(null=True)),
                ('text_en', models.TextField(null=True)),
                ('text_pt', models.TextField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Data de publicação (selecione no futuro para agendar)')),
                ('is_deleted', models.BooleanField(db_index=True, default=False, verbose_name='Ocultado?')),
                ('is_deleted_de', models.BooleanField(db_index=True, default=False, verbose_name='Ocultado?')),
                ('is_deleted_en', models.BooleanField(db_index=True, default=False, verbose_name='Ocultado?')),
                ('is_deleted_pt', models.BooleanField(db_index=True, default=False, verbose_name='Ocultado?')),
                ('instagram_posted', models.BooleanField(default=False)),
                ('facebook_posted', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='FreiRui.categories', verbose_name='Categoria da postagem')),
                ('galleries', models.ManyToManyField(blank=True, to='FreiRui.galleries')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=FreiRui.models.Images.get_image_filename, verbose_name='Images')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FreiRui.galleries')),
            ],
        ),
    ]
