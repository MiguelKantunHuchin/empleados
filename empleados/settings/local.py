from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "dbEmpleado",
        "USER": "miguel",
        "PASSWORD": "LJ260399",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

#! Se crea una ruta donde se almacenarán las fotos, similar a la ruta static
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
