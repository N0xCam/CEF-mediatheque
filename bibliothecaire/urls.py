from django.urls import path
from . import views


app_name = "bibliothecaire"

urlpatterns = [
    path('membres/', views.liste_membres, name='liste_membres'),
    path('ajouter_membre/', views.ajouter_membre, name='ajouter_membre'),
    path('medias/', views.liste_medias, name='liste_medias'),
    path('ajouter_media/', views.ajouter_media, name='ajouter_media'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('login/', views.login, name="login"),
    path('medias/', views.liste_medias, name='liste_medias'),
    path('medias/modifier/<int:media_id>/', views.modifier_media, name='modifier_media'),
    path('medias/supprimer/<int:media_id>/', views.supprimer_media, name='supprimer_media'),
    path('medias/emprunter/<int:media_id>/', views.emprunter_media, name='emprunter_media'),  # à venir

]
