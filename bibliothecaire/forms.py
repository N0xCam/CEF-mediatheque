from django import forms
from .models import ModelA, ModelB, Membre



class MembreForm(forms.ModelForm):
    class Meta :
        model = Membre
        fields = ['nom', 'email']

class ModelAForm(forms.ModelForm):
    class Meta :
        model = ModelA
        fields = ['type_media', 'titre', 'auteur']

class ModelBForm(forms.ModelForm):
    class Meta :
        model = ModelB
        fields = ['titre', 'auteur']

