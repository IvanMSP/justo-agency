import os
from .base import *
from decouple import config

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("NAMEDB"),
        "USER": config("USERDB"),
        "PASSWORD": config("PASSWORDDB"),
        "HOST": config("HOST"),
        "PORT": config("PORT"),
    },
}
