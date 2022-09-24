# Generated by Django 4.0.5 on 2022-09-24 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('author_album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to=settings.AUTH_USER_MODEL, verbose_name='Автор альбома')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
                'db_table': 'albums',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='fotos', verbose_name='Фотография')),
                ('signature', models.CharField(max_length=30, verbose_name='Подпись')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='webapp.album', verbose_name='Статья')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
                'db_table': 'photos',
            },
        ),
    ]