from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accueil, name='accueil'),
    path("bibliothecaire/", include('bibliothecaire.urls', namespace='bibliothecaire')),
    path("membre/", include("membre.urls", namespace='membre')),
]
