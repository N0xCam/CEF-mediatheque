from django import forms
from .models import Membre, Media, CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class User : CustomUser
    fields = ['username', 'email', 'role', 'password1', 'password2']

class MembreForm(forms.ModelForm):
    class Meta :
        model = Membre
        fields = ['nom', 'email']

class MediaForm(forms.ModelForm):
    class MediaMeta :
        model = Media
        fields = ['type_media', 'titre', 'auteur', 'disponible']

