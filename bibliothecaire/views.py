from sys import prefix
from django.shortcuts import render, redirect
from .forms import MembreForm, ModelAForm, ModelBForm
from .models import ModelA, ModelB, Membre
from django.contrib.auth.decorators import login_required

def dashboard(request):
    return render(request, 'dashboard.html')

def liste_membres(request):
    membres = Membre.objects.all()
    return render (request, 'liste_membres.html', {'membres' : membres})

def ajouter_membre(request):
    if request.method == "POST":
        form = MembreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_membres')
    else: form = MembreForm()
    return render(request, 'liste_membres.html', {'form' : form})

def ajouter_media(request):
    if request.method == "POST":
        form = ModelAForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('liste_medias')
    else: form = ModelAForm
    return render(request, 'ajouter_media.html', {'form': form})

def ajouter_jeu_plateau(request):
    if request.method == "POST":
        form = ModelBForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('liste_medias_jeu_plateau')
    else: form = ModelBForm
    return render(request, 'ajouter_jeu_plateau.html', {'form': form})


def liste_medias(request):
    medias = ModelA.objects.all(),
    return render(request, 'liste_medias.html', {'medias' : medias})

def liste_medias_jeux_plateaux(request):
    jeuxMedias = ModelB.objects.all(),
    return render(request, 'liste_medias_jeu_plateau.html', {'jeuxMedias': jeuxMedias})

