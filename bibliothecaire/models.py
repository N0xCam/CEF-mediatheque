from django.db import models


# Modèle Membre
class Membre(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_inscription = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nom

#Modèle Média empruntable
class ModelA(models.Model):
    TYPE_CHOICES = [
        ('livre', 'Livre'),
        ('dvd', 'Dvd'),
        ('cd', 'Cd'),
    ]
    titre = models.CharField(max_length=255)
    auteur = models.CharField(max_length=255)
    type_media = models.CharField(max_length=20, choices=TYPE_CHOICES)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f" {self.type_media} - {self.titre} - {self.auteur})"

#Modèle Média non empruntable
class ModelB(models.Model):
    titre = models.CharField(max_length=255)
    auteur = models.CharField(max_length=255)

    def __str__(self):
        return f" {self.titre} - {self.auteur})"

#Modèle Emprunt
