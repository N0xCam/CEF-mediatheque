from django.shortcuts import render, redirect
from .models import Membre

def liste_membres(request):
    membres = Membre.objects.all()
    return render (request, 'bibliothecaire/templates/liste_membres.html', {'membres' : membres})
