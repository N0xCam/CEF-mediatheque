from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils.timezone import now
from .utils import exporter_medias_en_json
from django.core.exceptions import ValidationError

# Modèle Membre
class Membre(models.Model):
    nom = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    date_inscription = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f" {self.nom}"

# Modèle CD
class CD(models.Model):
    artiste = models.CharField(max_length=100, null=True, blank=True)
    titre = models.CharField(max_length=200, null=True, blank=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f" {self.titre}"

# Modèle DVD
class DVD(models.Model):
    titre = models.CharField(max_length=100, null=True, blank=True)
    realisateur = models.CharField(max_length=100, null=True, blank=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f" {self.titre}"

# Modèle Livre
class Livre(models.Model):
    titre = models.CharField(max_length=100, null=True, blank=True)
    auteur = models.CharField(max_length=100, null=True, blank=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f" {self.titre}"

# Modèle Jeu de plateau
class JeuDePlateau(models.Model):
    titre = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.titre

# Modèle Utilisateur
class Bibliothecaire(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    related_name='bibliothecaire_user'

    def __str__(self):
        return self.user.username

    @classmethod
    def create(cls, username, password, email=""):
        Bibliothecaire.objects.create_user(username, email, password)

#Modèle Médias
class Media(models.Model):
    titre = models.CharField(max_length=200, null=True, blank=True)
    disponible = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.titre

    def get_type_media(self):
        if hasattr(self, 'livre'):
            return 'livre'
        elif hasattr(self, 'cd'):
            return 'cd'
        elif hasattr(self, 'dvd'):
            return 'dvd'
        return 'inconnu'

#Modèles emprunt
class Emprunt(models.Model):
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, null=True, blank=True, on_delete=models.CASCADE)
    cd = models.ForeignKey(CD, null=True, blank=True, on_delete=models.CASCADE)
    dvd = models.ForeignKey(DVD, null=True, blank=True, on_delete=models.CASCADE)
    date_emprunt = models.DateField(default=now)
    date_retour = models.DateField()

    def clean(self):
        medias = [self.livre, self.cd, self.dvd]
        if sum(1 for m in medias if m is not None) != 1:
            raise ValidationError("sélectionner exactement un média (Livre, CD ou DVD).")

    def save(self, *args, **kwargs):
        self.full_clean() # Appelle clean() avant de sauvegarder

        if not self.pk: # C’est un nouvel emprunt
            emprunts_actifs = Emprunt.objects.filter(
                membre=self.membre,
                date_retour__gte=timezone.now().date()
            ).count()
            if emprunts_actifs >= 3:
                raise ValidationError("Ce membre a déjà emprunté 3 médias.")

            if self.date_retour > self.date_emprunt + timedelta(days=7):
                raise ValidationError("La durée maximale d’un emprunt est de 7 jours.")

        super().save(*args, **kwargs)

@receiver([post_save, post_delete], sender=Livre)
@receiver([post_save, post_delete], sender=CD)
@receiver([post_save, post_delete], sender=DVD)
@receiver([post_save, post_delete], sender=JeuDePlateau)
def update_json_on_media_change(sender, instance, **kwargs):
    exporter_medias_en_json()