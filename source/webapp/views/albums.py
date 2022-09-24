from django.views.generic import ListView

from webapp.models import Album


class AlbumsView(ListView):
    model = Album
    template_name = "albums/albums_index.html"
    context_object_name = "albums"
    ordering = "-created_at"