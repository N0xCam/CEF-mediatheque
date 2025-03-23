from django import forms
from .models import Membre, Media

class MembreForm(forms.ModelForm):
    class Meta :
        model = Membre
        fields = ['nom', 'email']

class MediaForm(forms.ModelForm):
    class MediaMeta :
        model = Media
        fields = ['type_media', 'titre', 'auteur', 'disponible']

