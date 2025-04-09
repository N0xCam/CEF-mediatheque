from datetime import timedelta
from sys import prefix

from django.contrib.auth import authenticate, login
from django.core.checks import messages
from django.forms import Media
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import MembreForm, MediaForm
from .models import Membre, Livre, CD, DVD, JeuDePlateau
from django.contrib.auth.decorators import login_required, user_passes_test
import json
import os
from django.conf import settings
from collections import defaultdict
from django.contrib import messages


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
    if request.method == 'POST':
        form = MembreForm(request.POST)
        if form.is_valid():
            form.save()  # Sauvegarde le membre
            messages.success(request, "Membre créé avec succès!")  # Message de succès
            form = MembreForm()
    else:
        form = MembreForm()

    return render(request, 'ajouter_membre.html', {'form': form})

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
    if request.method == "POST":
        # Récupérer les données du formulaire
        type_media = request.POST.get("type")
        titre = request.POST.get("title")
        auteur = request.POST.get("auteur")  # Par exemple pour un livre
        artiste = request.POST.get("artiste")  # Pour un CD
        realisateur = request.POST.get("realisateur") # Pour un DVD
        description = request.POST.get("description")  # Pour un jeu de plateau
        print(f"Type de média: {type_media}, Titre: {titre}")  # Logs pour vérifier les données envoyées

        # Créer un dictionnaire pour le média
        nouveau_media = {
            "type": type_media,
            "title": titre,
        }

        if type_media == "livre":
            nouveau_media["auteur"] = auteur
        elif type_media == "cd":
            nouveau_media["artiste"] = artiste
        elif type_media == "dvd":
            nouveau_media["realisateur"] = realisateur
        elif type_media == "jeu de plateau":
            nouveau_media["description"] = description

        # Charger le fichier JSON existant pour ajouter le nouveau média
        chemin_fichier = os.path.join(settings.BASE_DIR, 'bibliothecaire', 'data', 'medias.json')

        try:
            with open(chemin_fichier, 'r+', encoding='utf-8') as f:
                # Charger les données actuelles du fichier JSON
                medias = json.load(f)
                print("Médias existants avant ajout:", medias)  # Logs pour vérifier le contenu du fichier

                # Ajouter le nouveau média
                medias.append(nouveau_media)

                # Revenir au début du fichier pour l'écrire à nouveau
                f.seek(0)
                json.dump(medias, f, ensure_ascii=False, indent=4)
                print("Média ajouté avec succès:", nouveau_media)  # Log de succès

            # Ajouter un message de succès
            messages.success(request, 'Média ajouté avec succès!')

        except Exception as e:
            # Log détaillé en cas d'erreur
            print("Erreur lors de l'ajout du média :", e)
            messages.error(request, f"Erreur lors de l'ajout du média: {e}")

    return render(request, 'ajouter_media.html')

def modifier_media(request, media_id):
    # Charger le média correspondant à l'id
    try:
        media = Media.objects.get(id=media_id)
    except Media.DoesNotExist:
        return HttpResponseNotFound("Média introuvable")

    # Ton code pour modifier le média
    if request.method == 'POST':
        # Effectuer les modifications et sauvegarder
        pass

    return render(request, 'modifier_media.html', {'media': media})

def liste_medias(request):
    chemin_fichier = os.path.join(settings.BASE_DIR, 'bibliothecaire', 'data', 'medias.json')

    listmedia = []

    try:
        with open(chemin_fichier, encoding='utf-8') as f:
            listmedia = json.load(f)
            print("Données chargées :", listmedia)  # Vérifie dans la console si les données sont chargées correctement
    except Exception as e:
        print("Erreur lors de la lecture du JSON :", e)

    return render(request, 'liste_medias.html', {'medias': listmedia})

def supprimer_media(request, media_id):
    # Cherche le média en fonction de l'ID
    media = get_object_or_404(Media, id=media_id)

    if request.method == 'POST':
        # Supprimer le média
        media.delete()  # Si tu utilises une base de données, sinon supprime du JSON
        return redirect('bibliothecaire:liste_medias')  # Redirige vers la liste des médias

    return render(request, 'supprimer_media.html', {'media': media})


from django.shortcuts import get_object_or_404, redirect
from .models import Media


def emprunter_media(request, media_id):
    # Cherche le média à emprunter
    media = get_object_or_404(Media, id=media_id)

    if request.method == 'POST':
        # Marque le média comme emprunté
        media.emprunté = True  # Assure-toi d'avoir ce champ dans ton modèle
        media.save()  # Sauvegarde la modification
        return redirect('bibliothecaire:liste_medias')  # Redirige vers la liste des médias

    return render(request, 'emprunter_media.html', {'media': media})