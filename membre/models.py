from django.db import models

class Media(models.Model):
    TYPE_CHOICES = [
        ('livre', 'Livre'),
        ('dvd', 'Dvd'),
        ('jeu de plateau', "Jeu de Plateau")
    ]
    titre = models.CharField(max_length=255)
    auteur = models.CharField(max_length=255)
    type_media = models.CharField(max_length=20, choices=TYPE_CHOICES)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f" {self.titre} - {self.auteur})"


# Create your models here.
