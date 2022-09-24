from django import forms
from django.forms import widgets

from webapp.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["image", "signature", "album"]


class PhotoDeleteForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["image", "signature", "album"]










