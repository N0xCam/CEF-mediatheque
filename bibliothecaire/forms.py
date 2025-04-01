from django import forms
from .models import Membre, Media
from django.contrib.auth.forms import UserCreationForm


class MembreForm(forms.ModelForm):
    class Meta :
        model = Membre
        fields = ['nom', 'email']

class MediaForm(forms.ModelForm):
    class MediaMeta :
        model = Media
        fields = ['type_media', 'titre', 'auteur', 'disponible']

