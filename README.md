# Personal Portfolio (Nuxt + Django)

This repository is now split into a modern frontend/backend architecture:

- `frontend/`: Nuxt (Vue) application for the portfolio UI.
- `backend/`: Django API + admin for projects, services, resume data, blog, and contact inquiries.
- `docker-compose.yml`: Local full-stack environment with PostgreSQL.

## What Changed

- Migrated from Django template monolith to split frontend + backend.
- Added **Services** section support via Django model + API.
- Added **Blog** section support via Django model + API.
- Added professional **Call-To-Action** flows:
  - Calendly integration (env-driven)
  - WhatsApp integration (env-driven)
- Switched Python dependency management from `pip` + `requirements.txt` to **`uv`** (`pyproject.toml` + `uv.lock`).
- Added Dockerfiles and Compose stack for local verification before production deployment.

## Backend (`backend/`)

### Environment

1. Copy env template:

```bash
cp .env.example .env
```

2. Update required variables in `.env`:
- `SECRET_KEY`
- `CONTACT_EMAIL`
- `CALENDLY_URL`
- `WHATSAPP_NUMBER`
- social links

### Install and run with `uv`

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py seed_resume_data
uv run python manage.py seed_projects
uv run python manage.py seed_site_content
uv run python manage.py runserver
```

API base URL (local): `http://localhost:8000/api/`

Useful endpoints:
- `/api/health/`
- `/api/config/`
- `/api/landing/`
- `/api/services/`
- `/api/projects/`
- `/api/resume/`
- `/api/blog/`
- `/api/blog/<slug>/`
- `/api/contact/`

## Frontend (`frontend/`)

### Environment

```bash
cp .env.example .env
```

Set:
- `API_BASE_URL` (server-side in Nuxt)
- `NUXT_PUBLIC_API_BASE_URL` (browser-side)

Default local values point to `http://localhost:8000/api`.

### Install and run

```bash
npm install
npm run dev
```

Frontend local URL: `http://localhost:3000`

## Docker Compose (recommended local full-stack check)

1. Ensure these files exist:
- `backend/.env.docker` (copy from `.env.docker.example`)
- `frontend/.env`

2. Start stack:

```bash
docker compose up --build
```

Services:
- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:8000/api/`
- Django admin: `http://localhost:8000/admin/`
- PostgreSQL: `localhost:5432`

## Testing

Backend tests:

```bash
cd backend
uv run python manage.py test
```

Frontend build/type check:

```bash
cd frontend
npm run build
npm run lint
```
