from datetime import timedelta
from sys import prefix

from django.contrib.auth import authenticate, login
from django.core.checks import messages
from django.forms import Media
from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import MembreForm, MediaForm, BibliothecaireLoginForm
from .models import Membre, Livre, CD, DVD, JeuDePlateau
from django.contrib.auth.decorators import login_required, user_passes_test
import json
import os
from django.conf import settings
from collections import defaultdict


#def is_bibliothecaire(user):
 #   return
  #  user.groups.filter(name='Bibliothecaire').exists()

def bibliothecaire_login(request):
    # Si l'utilisateur est déjà connecté, Redirection vers le dashboard
    if request.user.is_authenticated:
        return redirect('bibliothecaire:dashboard')  # Redirection vers le dashboard

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authentification de l'utilisateur
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Connexion de l'utilisateur
            return redirect('bibliothecaire:dashboard')  # Redirection vers le dashboard après login
        else:
            # Si l'authentification échoue
            error_message = 'Nom d\'utilisateur ou mot de passe incorrect.'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
#@user_passes_test(is_bibliothecaire)
def liste_membres(request):
    membres = Membre.objects.all()
    return render (request, 'liste_membres.html', {'membres' : membres})

@login_required
#@user_passes_test(is_bibliothecaire)
def ajouter_membre(request):
    if request.method == "POST":
        form = MembreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_membres')
    else: form = MembreForm()
    return render(request, 'liste_membres.html', {'form' : form})

@login_required
#@user_passes_test(is_bibliothecaire)
def medias_bibliothecaire(request):
    livres = Livre.objects.all()
    dvds = DVD.objects.all()
    cds = CD.objects.all()
    jeux_plateau = JeuDePlateau.objects.all()

    tous_les_medias = list(livres) + list(dvds) + list(cds) + list(jeux_plateau)

    return render(request, 'medias.html', {'medias' : tous_les_medias})

@login_required
#@user_passes_test(is_bibliothecaire)
def ajouter_media(request):
    if request.method == 'POST':
        form = MediaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_medias')  # Remplace 'liste_medias' si ton URL porte un autre nom
    else:
        form = MediaForm()

    return render(request, 'ajouter_media.html', {'form': form})

def liste_medias(request):
    chemin_fichier = os.path.join(settings.BASE_DIR, 'bibliothecaire', 'data', 'medias.json')  # sans accent

    listmedia = []
    medias_par_type = {}

    try:
        with open(chemin_fichier, encoding='utf-8') as f:
            listmedia = json.load(f)
            print("Données chargées :", listmedia)
    except Exception as e:
        print("Erreur lors de la lecture du JSON :", e)

    # Trie les médias par type
    for media in listmedia:
        type_media = media.get("type", "autre").lower()
        if type_media not in medias_par_type:
            medias_par_type[type_media] = []
        medias_par_type[type_media].append(media)

    print("Médias triés :", medias_par_type)
    return render(request, 'liste_medias.html', {'medias_par_type': medias_par_type})