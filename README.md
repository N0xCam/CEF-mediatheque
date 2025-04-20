Username : admin
Mot de passe : Books4ever

Ce projet de médiathèque a représenté un vrai défi, mais aussi une belle opportunité d’apprentissage. Le code de départ proposait une structure très simple en Python, avec quelques classes et un affichage console. J’ai choisi de le réinterpréter entièrement sous Django afin d’en faire une application web fonctionnelle et complète.
Ce projet m’a demandé beaucoup de temps et d’implication, mais il m’a permis de mieux comprendre Django, de mettre en pratique la structuration d’un projet web et de gagner en autonomie dans la résolution de problèmes techniques.
Je suis fière d’avoir mené ce projet à terme de manière autonome, et même si cela n’a pas été de tout repos, j’en ressors avec de nouvelles compétences solides.

    1. Étude et correctifs du code fourni

Le code d’origine était très rudimentaire, non adapté à un environnement web. J’ai donc repris l’intégralité de la logique pour l’adapter à Django. Le code fourni ne comportait ni gestion de base de données, ni modèles solides, ni possibilité d’interaction utilisateur autre que via le terminal.

Les correctifs apportés :

Refonte complète de l’architecture en suivant le modèle MVC de Django

Création de modèles pour les entités Livre, CD, DVD, JeuDePlateau, Membre, Emprunt

Mise en place d’un système de sessions, de droits d’accès et de formulaires web

    2. Mise en place des fonctionnalités demandées

Ajout, modification, suppression de membres et de médias

Possibilité d’emprunter un média (livre, CD ou DVD) avec une durée maximale de 7 jours.
Limitation à 3 emprunts actifs par membre.
Les jeux de plateaux ne sont pas empruntables.

Gestion des retours (modification automatique de la date de retour)

Vue pour les membres afin de consulter tous les médias disponibles

Interface spécifique pour les bibliothécaires avec authentification obligatoire

    3. Stratégie de tests

Des tests unitaires ont été réalisés sur les modèles pour vérifier les règles de gestion, notamment :

impossibilité de créer un emprunt avec plusieurs médias

limite d’emprunts actifs par membre

limite de durée d’emprunt

Des tests manuels ont aussi été réalisés sur l’interface (formulaires, redirections, affichage des données).

    4. Base de données de test

Une base de données a été constituée à partir de fixtures JSON, contenant plusieurs membres, médias de tous types et quelques emprunts déjà en cours. Cette base a permis de vérifier le bon affichage des listes et le bon fonctionnement des contraintes.

    5. Instructions d’exécution du projet

A. Cloner le projet depuis le repository GitHub :

git clone (https://github.com/N0xCam/CEF-mediatheque)

B. Créer un environnement virtuel et l’activer :

python -m venv venv
source venv/bin/activate # sous Unix/macOS
venv\Scripts\activate # sous Windows

C. Installer les dépendances :

pip install -r requirements.txt

D. Appliquer les migrations et charger les données de test :

python manage.py migrate
python manage.py loaddata bibliothecaire/fixtures/medias.json
python manage.py loaddata membre/fixtures/membres.json
python manage.py loaddata bibliothecaire/fixtures/emprunts.json

E. Lancer le serveur de développement :

python manage.py runserver

F. Accéder à l’application via http://127.0.0.1:8000/


