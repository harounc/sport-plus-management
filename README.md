# Sport Plus Management

Site vitrine Django/TailwindCSS fidèle au handoff client : pages publiques, galerie filtrable, fiches joueurs, actualités, formulaire e-mail et administration des contenus.

## Installation

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python manage.py migrate
.venv/bin/python manage.py createsuperuser
.venv/bin/python manage.py runserver
```

Le site est accessible sur `http://127.0.0.1:8000/` et l’administration sur `/admin/`. La migration charge les contenus de démonstration du prototype.

## Configuration

Variables disponibles : `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, `DJANGO_ALLOWED_HOSTS`, `EMAIL_BACKEND`, `DEFAULT_FROM_EMAIL` et `CONTACT_EMAIL`. Par défaut, les e-mails sont écrits dans la console de développement. En production, configurez un backend SMTP et servez les fichiers statiques avec le serveur web.

Les noms des deux associés, coordonnées et visuels sont explicitement provisoires et doivent être remplacés via l’administration avant la mise en ligne.
