# Atlas Sanctum Observatory

A Django semester project and working prototype for an intelligence observatory — a system for collecting, organising, and presenting signals about conditions that matter.

---

## Overview

The Observatory collects **Intelligence Signals**: observations about water, infrastructure, ecology, food, energy, climate, community, and health systems. Each signal can be tracked from initial observation through to verified, actionable, or resolved status.

This repository is the first working foundation of the Atlas Sanctum concept.

---

## Vision

Atlas Sanctum is exploring ethical digital infrastructure for sustainable development, shared prosperity, resilience, and measurable impact.

The Observatory is the first layer: a reliable system for surfacing and organising signals before they are lost.

---

## Core loop

```
Observe → Understand → Decide → Coordinate → Learn
```

---

## Features

- Django project with `config/` configuration folder
- `observatory` app registered in `INSTALLED_APPS`
- `IntelligenceSignal` model with category, status, location, source, and timestamps
- Database-backed signal listing at `/signals/`
- Signal detail pages at `/signals/<id>/`
- Django admin with list display, filtering, and search
- Project-level templates (`base.html`, `about.html`)
- App-level templates (`home.html`, `signals.html`, `signal_detail.html`)
- Template inheritance throughout
- Named URLs using `{% url %}` tags
- Demo data management command
- Full test suite

---

## Architecture

```
atlas-sanctum-django/
│
├── .gitignore
├── README.md
├── requirements.txt
├── manage.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── observatory/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── tests.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   └── 0002_add_location_source_updated_at.py
│   ├── management/
│   │   └── commands/
│   │       └── seed_demo_data.py
│   └── templates/
│       └── observatory/
│           ├── home.html
│           ├── signals.html
│           └── signal_detail.html
│
├── templates/
│   ├── base.html
│   └── about.html
│
└── static/
    └── site.css
```

---

## Installation

```bash
git clone <repository-url>
cd atlas-sanctum-django

python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

python -m pip install -r requirements.txt
python manage.py migrate
```

### Optional: load demonstration data

```bash
python manage.py seed_demo_data
```

All seeded records are clearly labelled as **Demo / Simulated** data.

---

## Run locally

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/`

---

## Testing

```bash
python manage.py test
```

Tests cover: homepage, signals list, signal detail (valid + 404), about page, and model creation.

---

## Routes

| URL | Description |
|-----|-------------|
| `/` | Observatory homepage |
| `/signals/` | Intelligence signal list (database-backed) |
| `/signals/<id>/` | Signal detail page |
| `/about/` | About the project |
| `/admin/` | Django admin |

---

## Academic purpose

This repository is a Django semester project demonstrating:

- Django project and app setup
- App registration in `INSTALLED_APPS`
- Database models and migrations
- Views, URLs, and template rendering
- App-level and project-level templates
- Template inheritance with `base.html`
- Django admin configuration
- Named URLs and `{% url %}` tags
- Git version control and GitHub-ready structure

---

## Security note

`DEBUG = True` is set for local development. Before any production deployment, set `DEBUG = False`, configure `ALLOWED_HOSTS`, and use a proper `SECRET_KEY` loaded from environment variables.

---

## Future roadmap

| Phase | Focus |
|-------|-------|
| 2 | Evidence management |
| 3 | Geospatial intelligence |
| 4 | Opportunity mapping |
| 5 | Decision support |
| 6 | AI-assisted analysis |
| 7 | Human-AI coordination |
| 8 | Impact measurement |
| 9 | Institutional collaboration |
| 10 | Regional / global intelligence infrastructure |
