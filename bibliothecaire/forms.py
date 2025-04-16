from telnetlib import AUTHENTICATION

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .models import Livre, DVD, CD, Membre, Media, JeuDePlateau

class BibliothecaireLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), label="Mot de passe", required=True)


#Formulaire de création de nouveaux membres
class MembreForm(forms.ModelForm):
    class Meta :
        model = Membre
        fields = ['nom', 'email']




class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = '__all__'

class CDForm(forms.ModelForm):
    class Meta:
        model = CD
        fields = '__all__'

class DVDForm(forms.ModelForm):
    class Meta:
        model = DVD
        fields = '__all__'

class JeuDePlateauForm(forms.ModelForm):
    class Meta:
        model = JeuDePlateau
        fields = '__all__'