"""
Django settings for api project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from json import JSONEncoder
from django.urls import reverse_lazy
from pathlib import Path
import os
import api.db as DB
import mimetypes


mimetypes.add_type("text/css", ".css", True)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-il7je)+vi237wmn5+&+edf9iqk_1h(8c)c2dtp&4sg3*etq467'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['127.0.0.1', '*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tinymce',
    #'login_example',
    #Custom Apps
    'core.delegacion',
    'core.lugar',
    'core.area_operativa',
    'core.eje_prevencion',
    'core.asignacion',
    'core.inicio',
    'core.notificacion',
    #'core.operacion',
    'core.reporte',
    'core.respuesta'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = DB.MySQL


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

LANGUAGE_CODE = 'es-gt'

TIME_ZONE = 'America/Guatemala'

USE_I18N = True

USE_TZ = True

#Ruta para imagenes
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

#Ruta para archivos estaticos CSS,JS,IMG
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '/static/')
STATICFILES_DIRS = [
    BASE_DIR / "static",
]



# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Default Auth_User Custom
AUTH_USER_MODEL='delegacion.Delegacion'


LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

JAZZMIN_SETTINGS = {
    'site_title':'PNC-SGPD',
    'site_brand':'PNC-SGPD',
    'site_header':'PNC-SGPD',
    'site_logo':'img/logo_pnc.png',
    'site_icon':'img/logo_pnc.ico',
    'welcome_sign':'¡Bienvenido!',
    "usermenu_links": [
        {"name": "Inicio", "url": "/", "new_window": False},
    ],

    'topmenu_links': [

        # Url that gets reversed (Permissions can be added)
        {'name':'Inicio','url':'/'},

        # model admin to link to (Permissions checked against model)
        #{"model": "auth.User"},

        
    ]
}