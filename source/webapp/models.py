from django.db import models
from django.contrib.auth import get_user_model


class Photo(models.Model):
    image = models.ImageField(upload_to="fotos", null=False, blank=False, verbose_name="Фотография")
    signature = models.CharField(max_length=30, null=False, blank=False, verbose_name="Подпись")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    author = models.ForeignKey(get_user_model(), null=False, blank=False, related_name="photos", verbose_name="Автор",
                               on_delete=models.CASCADE)
    album = models.ForeignKey("webapp.Album", null=True, blank=True, on_delete=models.CASCADE, related_name="albums_photo",
                              verbose_name="Альбом")

    def __str__(self):
        return f"{self.id}. {self.image}. {self.signature}. {self.created_at}. {self.album}. {self.author}"

    class Meta:
        db_table = "photos"
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"


class Album(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False, verbose_name="Название")
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name="Описание")
    author_album = models.ForeignKey(get_user_model(), null=False, blank=False, related_name="albums",
                                     verbose_name="Автор альбома",
                                     on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")


    def __str__(self):
        return f"{self.id}. {self.name}. {self.description}. {self.author_album}. {self.created_at}. "

    class Meta:
        db_table = "albums"
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"
