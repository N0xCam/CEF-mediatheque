from django.contrib import admin
from django.urls import path, include

#from bibliothecaire.views import bibliothecaire_login
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accueil, name='accueil'),
    path("bibliothecaire/", include('bibliothecaire.urls', namespace='bibliothecaire')),
    path("membre/", include("membre.urls", namespace='membre')),
  #  path('login/', bibliothecaire_login, name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html')),
]
