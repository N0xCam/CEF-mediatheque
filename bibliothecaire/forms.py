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


def ajouter_media(request):
    if request.method == 'POST':
        form = MediaForm(request.POST)
        if form.is_valid():
            form.save()  # Sauver le média dans la base
            return redirect('liste_medias')  # Rediriger vers la page de la liste des médias
    else:
        form = MediaForm()

    return render(request, 'ajouter_media.html', {'form': form})



class MediaForm(forms.Form):
    TYPE_CHOICES = [
        ('livre', 'Livre'),
        ('dvd', 'DVD'),
        ('cd', 'CD'),
        ('jeu_de_plateau', 'Jeu de Plateau'),
    ]

    type_media = forms.ChoiceField(choices=TYPE_CHOICES, required=True)
    titre = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)

    def save(self):
        type_media = self.cleaned_data.get('type_media')
        titre = self.cleaned_data.get('titre')
        description = self.cleaned_data.get('description')

        if type_media == 'livre':
            return Livre.objects.create(titre=titre, description=description)
        elif type_media == 'dvd':
            return DVD.objects.create(titre=titre, description=description)
        elif type_media == 'cd':
            return CD.objects.create(titre=titre, description=description)
        elif type_media == 'jeu_de_plateau':
            return JeuDePlateau.objects.create(titre=titre, description=description)