from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView


from webapp.forms import AlbumForm
from webapp.models import Album


class AlbumsView(ListView):
    model = Album
    template_name = "albums/albums_index.html"
    context_object_name = "albums"
    ordering = "-created_at"


class AlbumView(DetailView):
    template_name = "albums/album_view.html"
    model = Album


class CreateAlbum(LoginRequiredMixin, CreateView):
    form_class = AlbumForm
    template_name = "albums/album_create.html"

    def form_valid(self, form):
        user = self.request.user
        form.instance.author_album = user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("webapp:album_view", kwargs={"pk": self.object.pk})


class UpdateAlbum(UpdateView):
    form_class = AlbumForm
    template_name = "albums/album_update.html"
    model = Album

    def get_success_url(self):
        return reverse("webapp:album_view", kwargs={"pk": self.object.pk})


class DeleteAlbum(DeleteView):
    model = Album
    template_name = "albums/album_delete.html"
    success_url = reverse_lazy('webapp:index')
