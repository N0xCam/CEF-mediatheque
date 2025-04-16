from datetime import timedelta, datetime
from sys import prefix

from django.contrib.auth import authenticate, login
from django.core.checks import messages
from django.core.exceptions import ValidationError
from django.forms import Media
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import MembreForm, LivreForm, CDForm, DVDForm, JeuDePlateauForm
from .models import Membre, Livre, CD, DVD, JeuDePlateau, Emprunt
from django.contrib.auth.decorators import login_required, user_passes_test
import json
import os
from django.conf import settings
from collections import defaultdict
from django.shortcuts import get_object_or_404, redirect
from .models import Media
from django.shortcuts import render
import json
from django.contrib import messages
from django.urls import reverse
import json
from django.shortcuts import render
from django.http import HttpResponse
from .forms import LivreForm
from django.conf import settings
import os
import json
import os
from django.conf import settings
from django.shortcuts import render



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
def liste_membres(request):
    membres = Membre.objects.all()
    return render(request, 'liste_membres.html', {'membres':membres})


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
def modifier_membre(request, membre_id):
    membre = get_object_or_404(Membre, pk=membre_id)

    if request.method == 'POST':
        form = MembreForm(request.POST, instance=membre)
        if form.is_valid():
            form.save()
            return redirect(reverse('bibliothecaire:liste_membres'))
    else:
        form = MembreForm(instance=membre)

    return render(request, 'modifier_membres.html', {'form': form})

@login_required
def supprimer_membre(request, membre_id):
    membre = get_object_or_404(Membre, pk=membre_id)
    membre.delete()
    messages.success(request, "Membre supprimé avec succès !") # Message de succès
    return redirect('bibliothecaire:liste_membres') # Redirection vers la liste des membres

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
@login_required
def ajouter_media(request):
    if request.method == "POST":
        # Récupérer les données du formulaire
        type_media = request.POST.get("type")
        titre = request.POST.get("title")
        auteur = request.POST.get("auteur") # Par exemple pour un livre
        artiste = request.POST.get("artiste") # Pour un CD
        realisateur = request.POST.get("realisateur") # Pour un DVD
        description = request.POST.get("description") # Pour un jeu de plateau
        print(f"Type de média: {type_media}, Titre: {titre}") # Logs pour vérifier les données envoyées

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
            # Création d'un JeuDePlateau
            jeu_plateau = JeuDePlateau.objects.create(titre=titre, description=description)
            jeu_plateau.save()
            # Ajouter un message de succès
            messages.success(request, 'Jeu de plateau ajouté avec succès!')
            return redirect('bibliothecaire:liste_medias') # Redirection après ajout

        # Charger le fichier JSON existant pour ajouter le nouveau média
        chemin_fichier = os.path.join(settings.BASE_DIR, 'bibliothecaire', 'data', 'medias.json')

        try:
            with open(chemin_fichier, 'r+', encoding='utf-8') as f:
                # Charger les données actuelles du fichier JSON
                medias = json.load(f)
                print("Médias existants avant ajout:", medias) # Logs pour vérifier le contenu du fichier

                # Ajouter le nouveau média
                medias.append(nouveau_media)

                # Revenir au début du fichier pour l'écrire à nouveau
                f.seek(0)
                json.dump(medias, f, ensure_ascii=False, indent=4)
                print("Média ajouté avec succès:", nouveau_media) # Log de succès

            # Ajouter un message de succès
            messages.success(request, 'Média ajouté avec succès!')

        except Exception as e:
            # Log détaillé en cas d'erreur
            print("Erreur lors de l'ajout du média :", e)
            messages.error(request, f"Erreur lors de l'ajout du média: {e}")

    return render(request, 'ajouter_media.html')


def liste_medias(request):
    medias = Media.objects.all()  # Tous les médias
    jeux_de_plateau = JeuDePlateau.objects.all()  # Tous les jeux de plateau

    all_items = list(medias) + list(jeux_de_plateau)  # Combine les deux listes
    return render(request, 'liste_medias.html', {'items': all_items})

def load_media_data():
    with open('bibliothecaire/data/medias.json', 'r') as file:
        return json.load(file)
    print(medias)
    return medias



def list_livres(request):
    livres = Livre.objects.all()
    all_items = list(livres)
    return render(request, 'livres.html', {'items': all_items})


def list_cds(request):
    medias = load_media_data()
    cds = [media for media in medias if media['type'] == 'cd']
    return render(request, 'cds.html', {'cds': cds})

def list_dvds(request):
    medias = load_media_data()
    dvds = [media for media in medias if media['type'] == 'dvd']
    return render(request, 'dvds.html', {'dvds': dvds})

def list_jeux(request):
    medias = load_media_data()
    jeux = [media for media in medias if media['type'] == 'jeu de plateau']
    return render(request, 'jeux.html', {'jeux': jeux})


def ajouter_livre(request):
    if request.method == "POST":
        titre = request.POST.get('titre')
        auteur = request.POST.get('auteur')
        date_publication = request.POST.get('date_publication')

        # Charger les données actuelles depuis le fichier JSON
        with open('medias.json', 'r') as f:
            medias = json.load(f)

        # Créer un nouveau livre avec un ID basé sur la taille actuelle de la liste
        nouveau_livre = {
            'id': len(medias) + 1,  # Générer l'ID après avoir chargé les données
            'type': 'livre',
            'titre': titre,
            'auteur': auteur,
        }

        # Ajouter le nouveau livre à la liste des médias
        medias.append(nouveau_livre)

        # Sauvegarder les données mises à jour dans le fichier JSON
        with open('medias.json', 'w') as f:
            json.dump(medias, f)

        return redirect('bibliothecaire:afficher_livres')  # Ou rediriger vers la page d'affichage des livres

    return render(request, 'ajouter_livre.html')

















# Modèle d'emprunt
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from datetime import timedelta
from .models import Media, Emprunt
from django.contrib import messages

@login_required
@login_required
def emprunter_media(request, id):
    # Récupérer le média par son ID
    media = get_object_or_404(Media, id=id)

    # Vérifier les emprunts existants pour le membre (membre connecté)
    membre = request.user  # Supposons que le membre est lié à l'utilisateur connecté

    # Vérifier si le membre a déjà 3 emprunts
    emprunts_en_cours = Emprunt.objects.filter(membre=membre, retour=False)
    if emprunts_en_cours.count() >= 3:
        return render(request, 'erreur_emprunt.html',
                      {'message': 'Vous ne pouvez pas emprunter plus de 3 médias à la fois.'})

    # Vérifier si le membre est en retard sur un emprunt
    emprunts_retard = Emprunt.objects.filter(membre=membre, retour=False, date_retourne__lt=timezone.now())
    if emprunts_retard.exists():
        return render(request, 'erreur_emprunt.html',
                      {'message': 'Vous avez un emprunt en retard, vous ne pouvez pas emprunter de nouveau média.'})

    # Si le média est déjà emprunté, retourner une erreur
    if media.emprunt_set.filter(retour=False).exists():
        return render(request, 'erreur_emprunt.html', {'message': 'Le média est déjà emprunté par un autre membre.'})

    # Créer un emprunt
    date_emprunt = timezone.now()
    date_retour = date_emprunt + timedelta(days=7)  # 7 jours de prêt

    Emprunt.objects.create(
        media=media,
        membre=membre,
        date_emprunt=date_emprunt,
        date_retourne=date_retour,
        retour=False
    )

    # Retourner à la page d'accueil ou à une page de confirmation
    return redirect('bibliothecaire:liste_medias')

def ajouter_livre(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            nouveau_livre = form.cleaned_data

            # Charger le fichier JSON
            chemin_fichier = os.path.join(settings.BASE_DIR, 'medias.json')
            try:
                with open(chemin_fichier, 'r', encoding='utf-8') as f:
                    medias = json.load(f)
            except FileNotFoundError:
                medias = []

            # Générer un nouvel ID
            if medias:
                nouvel_id = max(item["id"] for item in medias) + 1
            else:
                nouvel_id = 1

            # Ajouter l'ID au livre
            nouveau_livre["id"] = nouvel_id
            nouveau_livre["type"] = "Livre"

            # Ajouter le livre à la liste et sauvegarder
            medias.append(nouveau_livre)

            with open(chemin_fichier, 'w', encoding='utf-8') as f:
                json.dump(medias, f, indent=4, ensure_ascii=False)

            return HttpResponse("Livre ajouté avec succès !")

    else:
        form = LivreForm()

    return render(request, 'ajouter_livre.html', {'form': form})

def ajouter_cd(request):
    if request.method == 'POST':
        form = CDForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cds')
    else:
        form = CDForm()
    return render(request, 'ajouter_cd.html', {'form': form})

def ajouter_dvd(request):
    if request.method == 'POST':
        form = DVDForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bibliothecaire:liste_dvds')
    else:
        form = DVDForm()
    return render(request, 'ajouter_dvd.html', {'form': form})

def ajouter_jeu(request):
    if request.method == 'POST':
        form = JeuDePlateauForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bibliothecaire:liste_jeux')
    else:
        form = JeuDePlateauForm()
    return render(request, 'ajouter_jeu.html', {'form': form})