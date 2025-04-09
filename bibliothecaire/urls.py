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

]
