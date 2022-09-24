from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from webapp.views.albums import AlbumsView
from webapp.views.photos import IndexView, PhotoView, CreatePhoto, UpdatePhoto, DeletePhoto

app_name = "webapp"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('photo/add/', CreatePhoto.as_view(), name="create_photo"),
    path('photo/<int:pk>/', PhotoView.as_view(), name="photo_view"),
    path('photo/<int:pk>/update/', UpdatePhoto.as_view(), name="update_photo"),
    path('photo/<int:pk>/delete/', DeletePhoto.as_view(), name="delete_photo"),
    path('albums/', AlbumsView.as_view(), name="album_index"),

    # path('article/<int:pk>/comment/add/', CreateCommentView.as_view(), name="article_comment_create"),
    # path('comments/<int:pk>/update/', UpdateComment.as_view(), name="update_comment"),
    # path('comments/<int:pk>/delete/', DeleteComment.as_view(), name="delete_comment"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
