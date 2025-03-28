from django.shortcuts import render, redirect
from .models import Membre, Media
from .forms import MembreForm, MediaForm
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_admin(request):
    return render(request, 'membre_dashboard.html')

@login_required
def dashboard_membre(request):
    return render(request, 'membres/membre_dashboard.html')

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