#!/bin/sh
export PATH=/usr/local/bin:/usr/bin:/bin
export PYTHONPATH=.

cd /var/www/softwaredeisign-rpi-gps/src
gunicorn -b 0.0.0.0:8000 gpsnow.wsgi:application
