from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from .models import Membre, Emprunt, CD, Livre, JeuDePlateau

#Formulaire pour la connexion des bibliothécaires
class BibliothecaireLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        print("KWARGS dans __init__ :", kwargs)
        kwargs.pop('fixtures', None) # protection temporaire
        super().__init__(*args, **kwargs)

    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), label="Mot de passe", required=True)


#Formulaire pour l'ajout de nouveaux membres
class MembreForm(forms.ModelForm):
    class Meta :
        model = Membre
        fields = ['nom', 'email']

#Formulaire pour l'ajout de nouveaux cds
class CDForm(forms.ModelForm):
    class Meta :
        model = CD
        fields = ['artiste', 'titre', 'disponible']

#Formulaire pour l'ajout de nouveaux dvds
class DVDForm(forms.ModelForm):
    class Meta :
        model = CD
        fields = ['artiste', 'titre', 'disponible']

#Formulaire pour l'ajout de nouveaux livres
class LivreForm(forms.ModelForm):
    class Meta :
        model = Livre
        fields = ['auteur', 'titre', 'disponible']

#Formulaire pour l'ajout de nouveaux jeux de plateaux
class JeuForm(forms.ModelForm):
    class Meta :
        model = JeuDePlateau
        fields = ['titre', 'description']

#Formulaire pour emprunter un média
class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['membre', 'livre', 'cd', 'dvd', 'date_retour']
