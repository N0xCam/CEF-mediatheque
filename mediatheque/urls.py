from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("bibliothecaire/", include("bibliothecaire.urls")),
    path("membre/", include("membre.urls")),
    path('', views.accueil, name='accueil'),
    path('dashboard/', views.dashboard_membre, name="dashboard"),
    path('connexion/', views.accueil, name='connexion'),
]
