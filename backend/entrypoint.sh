#!/bin/sh
set -e

echo "🚀 Starting application..."

# Optional DB check (fast fail if broken)
python - <<EOF
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.db import connection
connection.ensure_connection()

print("✅ Database connected")
EOF

echo "🌐 Starting Gunicorn..."

exec gunicorn config.wsgi:application \
  --bind 0.0.0.0:8080 \
  --workers 2 \
  --threads 4 \
  --timeout 120