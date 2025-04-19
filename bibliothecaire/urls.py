from . import views
from django.contrib.auth.views import LoginView
#from .forms import BibliothecaireLoginForm
from django.urls import path
from .views import (
    LivreListView,
    LivreCreateView,
    #CDListView,
    CDCreateView,
    DVDListView,
    DVDCreateView,
    JeuListView,
    JeuCreateView,
    retourner_emprunt
)

app_name = "bibliothecaire"

urlpatterns = [
    #Bibliothécaire : identification + tableau de bord
    path('dashboard/', views.dashboard, name="dashboard"),
  #  path('login/', LoginView.as_view(authenfication_form=BibliothecaireLoginForm), name="login"),


    #Gestion des membres
    path('membres/', views.liste_membres, name='liste_membres'),
    path('ajouter_membre/', views.ajouter_membre, name='ajouter_membre'),
    path('membres/modifier/<int:membre_id>/', views.modifier_membre, name='modifier_membre'),
    path('membres/supprimer/<int:membre_id>/', views.supprimer_membre, name='supprimer_membre'),

    #Gestion des médias
    path('livres/', LivreListView.as_view(), name='livres_liste'),
    path('livres/ajouter/', LivreCreateView.as_view(), name='livre_ajouter'),
    path('cds/', views.liste_cds, name='cds_liste'),
   # path('cds/ajouter/', views.ajouter_cd, name='ajouter_cd'),
    path('ajouter/cd/', views.ajouter_cd, name='ajouter_cd'),
    path('dvds/', DVDListView.as_view(), name='dvds_liste'),
    path('dvds/ajouter/', DVDCreateView.as_view(), name='dvd_ajouter'),
    path('jeux/', JeuListView.as_view(), name='jeux_liste'),
    path('jeux/ajouter/', JeuCreateView.as_view(), name='jeu_ajouter'),

    #Emprunts
    path('emprunts/', views.emprunt_liste, name='emprunts_liste'),
    path('emprunt/ajouter/', views.emprunt_ajouter, name='emprunt_ajouter'),
    path('emprunts/<int:emprunt_id>/retour/', retourner_emprunt, name='retour_emprunt'),
]


