from django import forms
from django.forms import widgets

from webapp.models import Photo, Album


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["image", "signature", "album"]


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["name", "description"]


class PhotoDeleteForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["image", "signature", "album"]
