from django.db import models

class Membre(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_inscription = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nom

# Create your models here.
