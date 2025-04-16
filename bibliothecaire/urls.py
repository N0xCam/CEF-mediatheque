from django.urls import path
from . import views


app_name = "bibliothecaire"

urlpatterns = [
    path('membres/', views.liste_membres, name='liste_membres'),
    path('ajouter_membre/', views.ajouter_membre, name='ajouter_membre'),


    path('ajouter_media/', views.ajouter_media, name='ajouter_media'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('login/', views.login, name="login"),
    path('medias/', views.liste_medias, name='liste_medias'),
    path('emprunter/<int:id>/', views.emprunter_media, name='emprunter_media'),
    path('membres/modifier/<int:membre_id>/', views.modifier_membre, name='modifier_membre'),
    path('membres/supprimer/<int:membre_id>/', views.supprimer_membre, name='supprimer_membre'),

    path('livres/', views.list_livres, name='livres'),
    path('cds/', views.list_cds, name='cds'),
    path('dvds/', views.list_dvds, name='dvds'),
    path('jeux/', views.list_jeux, name='jeux'),
    path('ajouter-livre/', views.ajouter_livre, name='ajouter_livre'),
    path('ajouter-cd/', views.ajouter_cd, name='ajouter_cd'),
    path('ajouter-dvd/', views.ajouter_dvd, name='ajouter_dvd'),
    path('ajouter-jeu/', views.ajouter_jeu, name='ajouter_jeu'),
]
