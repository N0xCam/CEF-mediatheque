from django.urls import path
from .views import liste_membres, ajouter_membre, ajouter_media, ajouter_jeu_plateau , dashboard, liste_medias,liste_medias_jeux_plateaux


app_name = "bibliothecaire"

urlpatterns = [
    path('membres/', liste_membres, name='liste_membres'),
    path('ajouter_membre/', ajouter_membre, name='ajouter_membre'),
    path('medias/', liste_medias, name='liste_medias'),
    path('medias_jeux_plateaux/', liste_medias_jeux_plateaux, name='liste_medias_jeux_plateaux'),
    path('ajouter_media/', ajouter_media, name='ajouter_media'),
    path('ajouter_jeu_plateau)/', ajouter_jeu_plateau, name='ajouter_jeu_plateau'),
    path('dashboard/', dashboard, name="dashboard"),

]
