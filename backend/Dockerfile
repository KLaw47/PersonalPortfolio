FROM python:3.12-slim

# Prevent python from writing .pyc files and using buffered stdout/stderr. prints logs straight to the console.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

#system deps for psycopg2 and such
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Django project
COPY . .

# Default command (dev server)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]