from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta

from .models import CD, Emprunt, Membre

class BibliothecaireTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # Données de base
        self.cd = CD.objects.create(titre="Test CD", artiste="Artiste Test")
        self.membre = Membre.objects.create(nom="Dupont", email="dupont@test.com")

    def test_dashboard_access(self):
        response = self.client.get(reverse('bibliothecaire:dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_ajout_cd(self):
        response = self.client.post(reverse('bibliothecaire:ajouter_cd'), {
            'titre': 'Nouveau CD',
            'artiste': 'Nouvel Artiste'
        })
        self.assertIn(response.status_code, [200, 302])

    def test_ajout_emprunt(self):
        response = self.client.post(reverse('bibliothecaire:emprunt_ajouter'), {
            'membre': self.membre.id,
            'cd': self.cd.id,
            'date_retour': timezone.now().date() + timedelta(days=7)
        })
        self.assertEqual(response.status_code, 302)

    def test_retour_emprunt(self):
        emprunt = Emprunt.objects.create(
            membre=self.membre,
            cd=self.cd,
            date_retour=timezone.now().date() + timedelta(days=7)
        )
        response = self.client.get(reverse('bibliothecaire:retour_emprunt', args=[emprunt.id]))
        self.assertEqual(response.status_code, 302)

    def test_affichage_liste_cds(self):
        response = self.client.get(reverse('bibliothecaire:liste_cds'))
        self.assertEqual(response.status_code, 200)