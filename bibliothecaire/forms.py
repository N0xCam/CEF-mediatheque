from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from .models import  Membre, Emprunt, CD

class BibliothecaireLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        print("KWARGS AVANT:", kwargs) # Ajoute ça pour voir ce qui entre
        kwargs.pop('fixtures', None)
        print("KWARGS APRES:", kwargs) # Et ça pour voir ce qui sort
        super().__init__(*args, **kwargs)

    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), label="Mot de passe", required=True)



#Formulaire de création de nouveaux membres
class MembreForm(forms.ModelForm):
    class Meta :
        model = Membre
        fields = ['nom', 'email']

#TEST
class CDForm(forms.ModelForm):
    class Meta :
        model = CD
        fields = ['artiste', 'titre', 'disponible']

class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['membre', 'livre', 'cd', 'dvd', 'date_retour']
