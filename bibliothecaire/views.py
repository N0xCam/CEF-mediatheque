from django.shortcuts import render, redirect
from .models import Membre
from .forms import MembreForm


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