from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.db.models import CharField
from django.forms import Media
from django.utils import timezone


# Modèle Membre
class Membre(models.Model):
    nom = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    date_inscription = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f" {self.nom}"


class Media(models.Model):
    titre = models.CharField(max_length=100, null=True, blank=True)
    emprunte = models.BooleanField(default=False)

    def get_type(self):
        return "Media" # On donne un nom simple pour le type

class JeuDePlateau(models.Model):
    titre = models.CharField(max_length=100, null=True, blank=True)
    auteur = models.CharField(max_length=100, null=True, blank=True)
    emprunte = models.BooleanField(default=False)

    def get_type(self):
        return "Jeu de Plateau"

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


class Bibliothecaire(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE),
    related_name='bibliothecaire_user'

    def __str__(self):
        return self.user.username

    @classmethod
    def create(cls, username, password, email=""):
        Bibliothecaire.objects.create_user(username, email, password)

class Emprunt(models.Model):
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    media = models.ForeignKey(Media,on_delete=models.CASCADE)
    date_emprunt = models.DateTimeField(auto_now_add=True)
    date_retour = models.DateTimeField()
    est_retourne = models.BooleanField(default=False)

    def est_en_retard(self):
        return timezone.now() > self.date_retour and not self.est_retourne

    def __str__(self):
        return f" Emprunt de {self.membre.nom} pour {self.media.titre}"

