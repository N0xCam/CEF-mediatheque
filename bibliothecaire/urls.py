from django.urls import path
from .views import liste_membres, ajouter_membre, liste_medias, ajouter_media, dashboard


app_name = "bibliothecaire"

urlpatterns = [
    path('membres/', liste_membres, name='liste_membres'),
    path('ajouter_membre/', ajouter_membre, name='ajouter_membre'),
    path('medias/', liste_medias, name='liste_medias'),
    path('ajouter_media/', ajouter_media, name='ajouter_media'),
    path('dashboard/', dashboard, name="dashboard"),

]
