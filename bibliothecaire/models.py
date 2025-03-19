from django.db import models

# Modèle Membre
class Membre(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_inscription = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nom

#Modèle Média
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
        return self.titre

#Modèle Emprunt
class Emprunt(models.Model):
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    date_emprunt = models.DateField(null=True, blank=True)

    def __str__(self):
        return f" {self.membre} a emprunté {self.media}"

