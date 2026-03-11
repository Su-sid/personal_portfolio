#!/bin/sh
set -eu

echo "Running database migrations..."
uv run python manage.py migrate --noinput

echo "Collecting static files..."
uv run python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
exec uv run gunicorn personal_portfolio.wsgi:application --config /app/gunicorn.conf.py
