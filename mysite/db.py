"""Database configuration helper for the Django project.

This module reads standard DB_* environment variables (DB_HOST, DB_PORT,
DB_USER, DB_PASSWORD, DB_NAME) and exposes a `DATABASES` setting compatible
with Django. If no `DB_NAME` is provided, it falls back to a local SQLite
database file at BASE_DIR / 'db.sqlite3'.

This makes it easy to run with Postgres when the container provides env vars
from docker-compose, and to use SQLite for local/development if none are set.
"""
from pathlib import Path
import environ
import os

# Read .env file if present and environment variables
env = environ.Env()
environ.Env.read_env()

# BASE_DIR should match settings.BASE_DIR (two levels up from this file)
BASE_DIR = Path(__file__).resolve().parent.parent

# If DB_NAME is set we assume a SQL database (Postgres by default)
db_name = env('DB_NAME', default=None)
if db_name:
    DATABASES = {
        'default': {
            'ENGINE': env('DB_ENGINE', default='django.db.backends.postgresql'),
            'NAME': db_name,
            'USER': env('DB_USER', default='postgres'),
            'PASSWORD': env('DB_PASSWORD', default=''),
            'HOST': env('DB_HOST', default='db'),
            'PORT': env('DB_PORT', default='5432'),
        }
    }
