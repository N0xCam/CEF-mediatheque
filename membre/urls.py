from django.urls import path
from . import views

urlpatterns = [
    path('medias/', views.liste_membres, name='liste_medias_membre'),
    path('membre_dashboard/', views.dashboard_membre, name="membre_dashboard"),
]