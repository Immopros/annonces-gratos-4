# AnnonceGratos (Django)

## Pages
- `/` : liste des annonces
- `/annonces/nouvelle/` : créer une annonce
- `/annonces/<id>/` : détail d’une annonce
- `/admin/` : administration

## Déploiement (Render)
Build command:
`pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`

Start command:
`gunicorn config.wsgi:application`
