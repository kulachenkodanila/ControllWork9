
from django.contrib import admin

from webapp.models import Photo, Album


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'signature', 'created_at', 'author', 'album']
    list_display_links = ['author', 'album']
    list_filter = ['created_at']
    search_fields = ['author']
    fields = ['image', 'signature', 'created_at', 'author', 'album']
    readonly_fields = ['created_at']


admin.site.register(Photo, PhotoAdmin)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'author_album', 'created_at']
    list_display_links = ['author_album', 'name']
    list_filter = ['created_at']
    search_fields = ['name']
    fields = ['name', 'description', 'author_album', 'created_at']
    readonly_fields = ['created_at']

admin.site.register(Album, AlbumAdmin)