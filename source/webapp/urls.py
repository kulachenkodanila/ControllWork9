from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from webapp.views.albums import AlbumsView, UpdateAlbum, AlbumView, CreateAlbum, DeleteAlbum
from webapp.views.photos import IndexView, PhotoView, CreatePhoto, UpdatePhoto, DeletePhoto

app_name = "webapp"





urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('photo/add/', CreatePhoto.as_view(), name="create_photo"),
    path('photo/<int:pk>/', PhotoView.as_view(), name="photo_view"),
    path('photo/<int:pk>/update/', UpdatePhoto.as_view(), name="update_photo"),
    path('photo/<int:pk>/delete/', DeletePhoto.as_view(), name="delete_photo"),
    path('albums/', AlbumsView.as_view(), name="album_index"),
    path('album/<int:pk>/update/', UpdateAlbum.as_view(), name="update_album"),
    path('album/<int:pk>/', AlbumView.as_view(), name="album_view"),
    path('album/add/', CreateAlbum.as_view(), name="create_album"),
    path('album/<int:pk>/delete/', DeleteAlbum.as_view(), name="delete_album"),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
