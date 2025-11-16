# Uni Planner (FYH)

A small Django project to manage meals, chores, habits and simple user accounts (register / login).

Contents
- `uni_planner/` — Django project
- `main/` — Django app containing views, forms, templates and static files

This README explains how to run the project locally and deploy to Vercel.

---

## Requirements
- Python 3.11+ (tested with 3.13 locally)
- PostgreSQL for production (optional for local development)
- See `requirements.txt` for Python dependencies

## Quick start (local development)

1. Create and activate a virtual environment

	```powershell
	python -m venv .venv
	.\.venv\Scripts\Activate.ps1
	```

2. Install dependencies

	```powershell
	python -m pip install -r requirements.txt
	```

3. (Optional) Create a `.env` file to set local environment overrides. Example:

	```text
	DEBUG=True
	SECRET_KEY=your-local-secret
	```

4. Run database migrations and collect static files

	```powershell
	python manage.py migrate
	python manage.py collectstatic --noinput
	```

5. Create a superuser (optional)

	```powershell
	python manage.py createsuperuser
	```

6. Run the development server

	```powershell
	python manage.py runserver
	```

Open http://127.0.0.1:8000/ in your browser.

---

## Project structure (important files)

- `uni_planner/settings.py` — Django settings (static config, database handling)
- `uni_planner/wsgi.py` / `api/index.py` — WSGI / Vercel entrypoint
- `uni_planner/urls.py` — project URLs (includes `main.urls`)
- `main/views.py`, `main/forms.py` — app views and forms (login/register)
- `main/templates/main/` — templates (`home.html`, `login.html`, `register.html`, etc.)
- `requirements.txt` — Python packages
- `vercel.json` — Vercel build & routing configuration

---

## Environment variables (production on Vercel)

Set these in Vercel Project Settings → Environment Variables (or provide them in your hosting platform):

- `DATABASE_URL` — Full Postgres connection URL (e.g. `postgres://user:password@host:5432/dbname`). If not set, the app defaults to a local SQLite DB for development.
- `SECRET_KEY` — Django secret key (do not commit into source control).
- `DEBUG` — `False` in production (string). The repo's `vercel.json` sets `DEBUG=false` by default, but set explicitly in project env.
- `ALLOWED_HOSTS` — optional comma-separated list of allowed hostnames.

## Vercel deployment notes

- `vercel.json` in the repo is configured to use `api/index.py` as the Python serverless entry point and to run a `buildCommand` that installs dependencies, runs migrations and collects static files.
- The repo uses WhiteNoise to serve static files. `STATIC_ROOT` and `STATICFILES_STORAGE` are configured in `settings.py`.
- IMPORTANT: SQLite is ephemeral on Vercel — use Postgres for production (`DATABASE_URL` set to a managed Postgres instance).

If you get `OperationalError: no such table: auth_user` on deploy, it means migrations did not run during the build. Check Vercel build logs for the `python manage.py migrate` output.

---

## Troubleshooting checklist

- Local site works but Vercel shows 404:
  - Verify Vercel build logs ran `migrate` and `collectstatic` successfully.
  - Ensure `api/index.py` exists and `vercel.json` routes `/` to it.

- Database connection errors:
  - Confirm `DATABASE_URL` is correct and the DB accepts connections from Vercel.

- Static/CSS broken on Vercel:
  - Confirm `collectstatic` ran and `staticfiles/` was created in the build output.
  - Check `STATICFILES_STORAGE` is set to a WhiteNoise storage class.

---

## Useful commands

- `python manage.py check` — run Django system checks
- `python manage.py migrate` — apply migrations
- `python manage.py createsuperuser` — create admin user
- `python manage.py collectstatic --noinput` — collect static files for production

---

If you want, I can add a `/health/` endpoint to the app for quick uptime checks, or create a `docker-compose.yml` to run local Postgres with the project. Which would you prefer?
