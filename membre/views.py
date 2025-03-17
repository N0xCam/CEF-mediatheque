from django.shortcuts import render
from bibliothecaire.models import Membre

def liste_membres(request):
    Membre = Membre.objects.filter(disponible=True)
    return render(request, 'membre/liste_membre.html', {'membre' : membres})

# Create your views here.
