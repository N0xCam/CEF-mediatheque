from django.urls import path
from . import views

urlpatterns = [
    path('medias/', views.liste_membres, name='liste_medias_membre')
]