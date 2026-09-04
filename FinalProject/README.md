# Bill-Splitting App (Django MVP)

Quickstart (development):

1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Run migrations and seed demo data

```powershell
python manage.py migrate
python manage.py seed
python manage.py runserver
```

3. Open http://127.0.0.1:8000/ in your browser.

Project layout:
- `finalproject/` - Django project settings and urls
- `expenses/` - main app with models, views, templates, and API

To run tests:

```powershell
pytest
```

Deployment: configure a Postgres database, set `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=0`, and use Render or Railway.
