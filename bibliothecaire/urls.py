from django.urls import path
from .views import liste_membres, ajouter_membre, liste_medias, ajouter_media, register, CustomLoginView, dashboard
from django.contrib.auth.views import LogoutView
from . import views

app_name = "bibliothecaire"

urlpatterns = [
    path('membres/', liste_membres, name='liste_membres'),
    path('ajouter_membre/', ajouter_membre, name='ajouter_membre'),
    path('medias/', liste_medias, name='liste_medias'),
    path('ajouter_media/', ajouter_media, name='ajouter_media'),
    path('dashboard/', dashboard, name="dashboard"),
    path('register/', register, name="register"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
