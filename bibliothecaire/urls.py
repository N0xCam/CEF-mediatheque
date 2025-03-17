from django.urls import path
from .views import liste_membres



urlpatterns = [
    path('membres/', liste_membres, name='membres'),

]
