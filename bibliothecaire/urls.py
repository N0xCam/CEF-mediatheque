from django.urls import path
from .views import liste_membres, ajouter_membre, liste_medias



urlpatterns = [
    path('membres/', liste_membres, name='liste_membres'),
    path('ajouter_membre/', ajouter_membre, name='ajouter_membre'),
    path('medias/', liste_medias, name='liste_medias'),
]
