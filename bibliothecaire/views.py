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
    return render(request, 'ajouter_membre.html', {'form' : form})

def ajouter_media(request):
    if request.method == 'POST':
        form_a = ModelAForm(request.POST),
        form_b = ModelBForm(request.POST),

        if form_a.is_valid():
            form_a.save()
        if form_b.is_valid():
            form_b.save()
    else:
        form_a = ModelAForm()
        form_b = ModelBForm()
    return render(request, 'ajouter_media.html', {'form_a': form_a}, {'form_b': form_b})

def liste_medias(request):
    medias = ModelA.objects.all(), ModelB.objects.all()
    return render(request, 'liste_medias.html', {'medias' : medias})


