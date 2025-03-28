from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from bibliothecaire.models import Membre

@login_required
def dashboard_membre(request):
    return render(request, 'membres/membre_dashboard.html')

def liste_membres(request):
    membre = Membre.objects.filter(disponible=True)
    return render(request, 'liste_medias.html', {'membre' : membre})

# Create your views here.
