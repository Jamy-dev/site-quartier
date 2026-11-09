# Guédiawaye — site du quartier (Django)

## Lancer en local
```
python -m venv venv
venv\Scripts\activate        # Windows  (Mac/Linux : source venv/bin/activate)
pip install -r requirements.txt
python manage.py runserver
```
Ouvre http://127.0.0.1:8000

## Modifier le site
- Textes et mise en page : `quartier/templates/quartier/index.html`
- Photos : dossier `quartier/static/quartier/img/`
- Titres, legendes et credits des photos : `quartier/views.py` (dictionnaire PHOTOS)

## Mise en ligne (Render, Railway, PythonAnywhere...)
- Commande de build : `pip install -r requirements.txt && python manage.py collectstatic --noinput`
- Commande de demarrage : `gunicorn guediawaye.wsgi`
- Variables : `DJANGO_SECRET_KEY` (phrase secrete), `DJANGO_DEBUG=0`, `DJANGO_ALLOWED_HOSTS=ton-domaine.com`

Les photos appartiennent a leurs auteurs (credits dans le pied de page).
