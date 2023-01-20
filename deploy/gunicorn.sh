#!/bin/bash
NAME="sgpd"
DJANGODIR=$(dirname $(cd `dirname $0` && pwd))
SOCKFILE=/tmp/gunicorn-sgpd.sock
LOGDIR=${DJANGODIR}/logs/gunicorn.log
USER=sgpd
GROUP=sgpd
NUM_WORKERS=5
DJANGO_WSGI_MODULE=api.wsgi

rm -frv $SOCKFILE
echo $DJANGODIR
cd $DJANGODIR
exec ${DJANGODIR}/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=$LOGDIR
