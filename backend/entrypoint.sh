#!/bin/sh

echo "Checking storages backend..."
python -c "import storages; print('storages is installed')"

echo "GS_BUCKET_NAME=$GS_BUCKET_NAME"

echo "Checking Django storage backend..."
python - <<EOF
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.conf import settings
print("STATICFILES_STORAGE:", settings.STATICFILES_STORAGE)
print("GS_BUCKET_NAME:", getattr(settings, "GS_BUCKET_NAME", None))
EOF

echo "Running collectstatic..."
python manage.py collectstatic --noinput --verbosity 3 || exit 1

echo "Starting Gunicorn..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8080