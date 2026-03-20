#!/bin/sh
set -e

echo "🚀 Starting application..."

# -------------------------------
# Verify dependencies
# -------------------------------

echo "🔍 Checking storages backend..."
python -c "import storages; print('✅ django-storages is installed')"

echo "📦 GS_BUCKET_NAME=${GS_BUCKET_NAME}"

# -------------------------------
# Verify Django storage settings
# -------------------------------

echo "🔍 Checking Django storage configuration..."
python - <<EOF
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.conf import settings

print("STATICFILES_STORAGE:", settings.STATICFILES_STORAGE)
print("GS_BUCKET_NAME:", getattr(settings, "GS_BUCKET_NAME", None))
EOF

# -------------------------------
# Collect static files
# -------------------------------

echo "📁 Running collectstatic..."
python manage.py migrate
python manage.py collectstatic --noinput --verbosity 2

# -------------------------------
# Check database connection
# -------------------------------

echo "🗄️ Checking database connection..."
python - <<EOF
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.db import connection

try:
connection.ensure_connection()
print("✅ Database connection successful")
except Exception as e:
print("❌ Database connection failed:")
print(e)
raise
EOF

# -------------------------------
# Start application
# -------------------------------

echo "🌐 Starting Gunicorn..."
exec gunicorn config.wsgi:application 
--bind 0.0.0.0:8080 
--workers 3 
--threads 2 
--timeout 120
