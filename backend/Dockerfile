FROM python:3.14-slim

# Prevent Python from buffering logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# System deps
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install deps
COPY pyproject.toml uv.lock ./
RUN pip install --no-cache-dir uv && uv sync --frozen --no-dev

# Copy project
COPY . .

# Set environment
ENV PATH="/app/.venv/bin:$PATH"

# Expose port 8080
EXPOSE 8080

# Run app with Gunicorn
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8080"]