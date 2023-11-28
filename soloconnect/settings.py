"""
Django settings for soloconnect project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-0jj-2ypgi=tz+(es1-6*%vqhd-90ft+#a%qzbz9yn8orneh@m7"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "172.31.31.138",
    "soloconnect-integration.us-east-1.elasticbeanstalk.com",
    "soloconnect-db-final.us-west-2.elasticbeanstalk.com",
    "soloconnect-production.us-east-1.elasticbeanstalk.com",
    "testserver",
    "soloconnect-chat-integration.us-east-1.elasticbeanstalk.com",
]

# Application definition

INSTALLED_APPS = [
    "daphne",
    "channels",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "home_default.apps.HomeDefaultConfig",
    "user_profile.apps.UserProfileConfig",
    "trip.apps.TripConfig",
    "crispy_forms",
    "crispy_bootstrap4",
    "matching.apps.MatchingConfig",
    "chat.apps.ChatConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "soloconnect.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "soloconnect.wsgi.application"
ASGI_APPLICATION = "soloconnect.asgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "PORT": os.getenv("RDS_PORT"),
        "USER": os.getenv("RDS_USERNAME"),
        "HOST": os.getenv("RDS_HOSTNAME"),
        "NAME": os.getenv("RDS_DB_NAME"),
        "PASSWORD": os.getenv("RDS_PASSWORD"),
        "ENGINE": "django.db.backends.postgresql",
        "TEST": {"NAME": "testdatabase2"},
    }
}
if "test" in sys.argv:
    DATABASES["default"] = {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": os.getenv("TEST_RDS_HOSTNAME"),
        "USER": os.getenv("TEST_RDS_USERNAME"),
        "PASSWORD": os.getenv("TEST_RDS_PASSWORD"),
        "NAME": os.getenv("TEST_RDS_DB_NAME"),
        "PORT": os.getenv("TEST_RDS_DB_PORT"),
        "TEST": {"NAME": "testdatabase2"},
    }
# if "test" in sys.argv:
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.sqlite3",
#              "NAME": "testmemory",
#         }
#     }
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_URL = "user_profile:login"
LOGIN_REDIRECT_URL = "user_profile:view_profile"

CRISPY_TEMPLATE_PACK = "bootstrap4"
# Email configs
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [
                (
                    "sc-redis.45ncis.ng.0001.use1.cache.amazonaws.com",
                    6379,
                )
            ],
        },
        "CACHES": {
            "default": {
                "BACKEND": "django.core.cache.backends.redis.RedisCache",
                "LOCATION": "redis://sc-redis.45ncis.ng.0001.use1.cache.amazonaws.com:6379/1",
            }
        },
    },
}
