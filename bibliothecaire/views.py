from django.shortcuts import render, redirect
from .models import Membre, Media
from .forms import MembreForm, MediaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.views import LoginView




@login_required
def dashboard(request):
    return render(request, 'bibliothecaire/dashboard.html')

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
    return render(request, 'liste_medias.html', {'medias' : medias})

def ajouter_media(request):
    if request.method == "POST":
        form = MediaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_medias')
    else: form = MediaForm()


