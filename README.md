# Atlas Sanctum Django Semester Project

## Project

**Atlas Sanctum Observatory** — a Django foundation for exploring how digital intelligence can help people observe systems, understand evidence, coordinate decisions, and learn from outcomes.

### Core philosophy

**Observe → Understand → Decide → Coordinate → Learn**

## Django requirements satisfied

- Django project configuration folder: `config/`
- Django app: `observatory/`
- `manage.py`
- App-level URLs: `observatory/urls.py`
- App-level template: `observatory/templates/observatory/home.html`
- Project-level templates: `templates/base.html`, `templates/about.html`
- Project-level template configuration in `config/settings.py`
- SQLite database excluded from Git
- Virtual environment excluded from Git

## Local setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Routes

- `/` — Observatory homepage (app view + app template)
- `/about/` — About page (project-level template)
- `/admin/` — Django admin

## Git

```bash
git init
git add .
git commit -m "Initial Django semester project"
```

## GitHub

Create an empty GitHub repository, then connect and push:

```bash
git remote add origin https://github.com/YOUR_USERNAME/atlas-sanctum-django.git
git branch -M main
git push -u origin main
```
