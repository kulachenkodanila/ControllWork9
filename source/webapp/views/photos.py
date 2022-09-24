from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PhotoForm, PhotoDeleteForm
from webapp.models import Photo


class IndexView(ListView):
    model = Photo
    template_name = "photos/index.html"
    context_object_name = "photos"
    ordering = "-created_at"


class PhotoView(DetailView):
    template_name = "photos/photo_view.html"
    model = Photo


class CreatePhoto(LoginRequiredMixin, CreateView):
    form_class = PhotoForm
    template_name = "photos/create.html"

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("webapp:photo_view", kwargs={"pk": self.object.pk})


class UpdatePhoto(PermissionRequiredMixin,UpdateView):
    form_class = PhotoForm
    template_name = "photos/update.html"
    model = Photo

    def get_success_url(self):
        return reverse("webapp:photo_view", kwargs={"pk": self.object.pk})


class DeletePhoto(DeleteView):
    model = Photo
    template_name = "photos/delete.html"
    success_url = reverse_lazy('webapp:index')


