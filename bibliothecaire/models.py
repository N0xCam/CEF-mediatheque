from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.db.models import CharField
from django.forms import Media
from django.utils import timezone


# Modèle Membre
class Membre(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_inscription = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nom


class Media(models.Model):
    titre = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    est_empruntable = models.BooleanField(null=True, blank=True)

    class Meta:
        verbose_name = "Média"
        verbose_name_plural = "Médias"

    def __str__(self):
        return self.titre

class Livre(Media):
    auteur = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f" {self.titre} - {self.auteur}"

class DVD(Media):
    realisateur = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f" {self.titre} - {self.realisateur}"

class CD(Media):
    artiste = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f" {self.titre} - {self.artiste}"

class JeuDePlateau(models.Model):
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f" {self.titre} - {self.description})"

class Bibliothecaire(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE),
    related_name='bibliothecaire_user'

    def __str__(self):
        return self.user.username

    @classmethod
    def create(cls, username, password, email=""):
        Bibliothecaire.objects.create_user(username, email, password)
