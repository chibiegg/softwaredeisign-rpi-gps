#!/bin/sh
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin
export PYTHONPATH=.

cd /home/pi/softwaredeisign-rpi-gps/src
python3 gpsrecv/__init__.py /dev/ttyAMA0 GPS01 http://gps.example.com:8000/trasponder/waypoint/
