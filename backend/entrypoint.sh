#!/bin/sh

echo "Running collectstatic..."
python manage.py collectstatic --noinput --verbosity 2

echo "Starting Gunicorn..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8080