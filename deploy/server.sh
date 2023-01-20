#!/bin/bash
DJANGODIR=$(dirname $(cd `dirname $0` && pwd))
DJANGO_SETTINGS_MODULE=api.settings
cd $DJANGODIR
source bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
exec python3 manage.py runserver 0:8000
