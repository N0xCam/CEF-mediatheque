Instructions d’exécution du projet

A. Cloner le projet depuis le repository GitHub :

git clone [lien_du_repo]

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

