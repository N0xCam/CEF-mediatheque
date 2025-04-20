from . import views
#from .forms import BibliothecaireLoginForm
from django.urls import path

from .forms import BibliothecaireLoginForm
from .views import (

    retourner_emprunt, bibliothecaire_login
)

app_name = "bibliothecaire"

urlpatterns = [
    #Bibliothécaire : identification + tableau de bord
    path('dashboard/', views.dashboard, name="dashboard"),
    path('login/', bibliothecaire_login,name="login"),


    #Gestion des membres
    path('membres/', views.liste_membres, name='liste_membres'),
    path('ajouter_membre/', views.ajouter_membre, name='ajouter_membre'),
    path('membres/modifier/<int:membre_id>/', views.modifier_membre, name='modifier_membre'),
    path('membres/supprimer/<int:membre_id>/', views.supprimer_membre, name='supprimer_membre'),

    #Gestion des médias
    path('livres/', views.liste_livres, name='liste_livres'),
    path('ajouter/livre/', views.ajouter_livre, name='ajouter_livre'),
    path('cds/', views.liste_cds, name='liste_cds'),
   # path('cds/ajouter/', views.ajouter_cd, name='ajouter_cd'),
    path('ajouter/cd/', views.ajouter_cd, name='ajouter_cd'),
    path('dvds/', views.liste_dvds, name='liste_dvds'),
    path('ajouter/dvd/', views.ajouter_dvd, name='ajouter_dvd'),
    path('jeux/', views.liste_jeux, name='liste_jeux'),
    path('ajouter/jeu/', views.ajouter_jeu, name='ajouter_jeu'),

    #Emprunts
    path('emprunts/', views.emprunt_liste, name='emprunts_liste'),
    path('emprunt/ajouter/', views.emprunt_ajouter, name='emprunt_ajouter'),
    path('emprunts/<int:emprunt_id>/retour/', retourner_emprunt, name='retour_emprunt'),
]


