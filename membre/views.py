from django.shortcuts import render
from bibliothecaire.models import ModelA, ModelB

def liste_medias(request):
    medias = ModelA.objects.all(), ModelB.objects.all()
    return render(request, 'liste_medias.html', {'medias' : medias})

# Create your views here.
