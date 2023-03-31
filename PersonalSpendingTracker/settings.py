"""
Django settings for PersonalSpendingTracker project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
from django.contrib.messages import constants as message_constants
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY'] if 'DJANGO_SECRET_KEY' in os.environ else 'django-insecure-mlmbekqz9+)p0o!*24akj0(ufh&v$w_d(9cj6j0&58=!v++5_e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'minted-aymskyt.azurewebsites.net']
CSRF_TRUSTED_ORIGINS = ['https://minted-aymskyt.azurewebsites.net']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'minted',
    'widget_tweaks',
    'webpush',
    'django_crontab',
    'django.contrib.sites',
    'django_cleanup.apps.CleanupConfig',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


SITE_ID = 2

ACCOUNT_USER_MODEL_USERNAME_FIELD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_CHOICE_SESSION_KEY = None

LOGIN_REDIRECT_URL = 'budget_sign_up'
LOGOUT_REDIRECT_URL = '/'

ACCOUNT_FORMS = {'signup': 'minted.forms.SignUpForm', 'login': 'minted.forms.LogInForm'}

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

CLIENT_ID = os.environ['CLIENT_ID']
SECRET = os.environ['SECRET']

EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_PORT = os.environ['EMAIL_PORT']
EMAIL_USE_TLS = os.environ['EMAIL_USE_TLS']

WEBPUSH_SETTINGS = {
   "VAPID_PUBLIC_KEY": os.environ['VAPID_PUBLIC_KEY'],
   "VAPID_PRIVATE_KEY": os.environ['VAPID_PRIVATE_KEY'],
   "VAPID_ADMIN_EMAIL": os.environ['VAPID_ADMIN_EMAIL']
}

CRONJOBS = [
    ('0 9 * * *', 'minted.cron.send_daily_notifications'), # Everyday at 9:00
    ('0 9 * * 0', 'minted.cron.send_weekly_notifications'), # Every Sunday at 9:00 
    ('0 9 1 * *', 'minted.cron.send_monthly_notifications'), # First day of every month at 9:00 
    ('0 0 * * *', 'minted.cron.give_budget_points'), #Everyday at midnight 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'PersonalSpendingTracker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

WSGI_APPLICATION = 'PersonalSpendingTracker.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

if not DEBUG:
    if 'DATABASE_NAME' in os.environ:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': os.environ['DATABASE_NAME'],
                'USER': os.environ['DATABASE_USER'],
                'PASSWORD': os.environ['DATABASE_PASSWORD'],
                'HOST': os.environ['DATABASE_HOST'],
                'PORT': os.environ['DATABASE_PORT'],
                'OPTIONS': {
                    'ssl': {'ca': os.environ['SSL_CERT_PATH']}
                }
            }
        }
    if 'AZURE_ACCOUNT_NAME' in os.environ:
        DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
        AZURE_ACCOUNT_NAME = os.environ['AZURE_ACCOUNT_NAME']
        AZURE_ACCOUNT_KEY = os.environ['AZURE_ACCOUNT_KEY']
        AZURE_CONTAINER = os.environ['AZURE_CONTAINER']


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#login url for redirecting user when not logged in
LOGIN_URL = 'log_in'

# Path for file uploads
UPLOAD_DIR = 'uploads/'
REWARDS_DIR = 'rewards/'
UPLOAD_ROOT = os.path.join(BASE_DIR, UPLOAD_DIR)
REWARDS_ROOT = os.path.join(BASE_DIR, REWARDS_DIR)

# URL for redirects
REDIRECT_URL_WHEN_LOGGED_IN_AS_USER = 'dashboard'
REDIRECT_URL_WHEN_LOGGED_IN_AS_ADMIN = 'rewards_list'

# Message level tags should use Bootstrap terms
MESSAGE_TAGS={
    message_constants.DEBUG : 'dark',
    message_constants.ERROR : 'danger',
}

# User model for authentication and login purposes
AUTH_USER_MODEL = 'minted.User'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]

#Page lengths
FRIENDS_PER_PAGE = 8
REQUESTS_PER_PAGE = 8
EXPENDITURES_PER_PAGE = 8
CATEGORIES_PER_PAGE = 8
BUDGETS_PER_PAGE = 4