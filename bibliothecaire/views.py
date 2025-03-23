from django.shortcuts import render, redirect
from .models import Membre, Media
from .forms import MembreForm, MediaForm


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

    return render(request, 'ajouter_membre.html', {'form' : form})

def liste_medias(request):
    medias = Media.objects.all()
    return render (request, 'liste_medias.html', {'media' : medias})

def ajouter_media(request):
    if request.method == "POST":
        form = MediaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_media')
    else: form = MediaForm()