from django.shortcuts import render
from bibliothecaire.models import CD, DVD, Livre, JeuDePlateau


def liste_medias(request):
    cds = CD.objects.all()
    dvds = DVD.objects.all()
    livres = Livre.objects.all()
    jeux = JeuDePlateau.objects.all()

    print("CDS:", cds)

    return render(request, 'membre/liste_medias.html', {'livres': livres,'jeux': jeux, 'cds': cds, 'dvds': dvds})

