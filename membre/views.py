from django.shortcuts import render
from bibliothecaire.models import Media

def liste_medias(request):
    medias = Media.objects.filter(disponible=True)
    return render(request, 'membre/liste_medias.html', {'medias' : medias})

# Create your views here.
