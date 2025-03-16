from django.urls import path
from .views import liste_membres
from django.http import HttpResponse


def membres(request):
    return HttpResponse("Test OK")

urlpatterns = [
    path('membres/', liste_membres, name='membres'),

]