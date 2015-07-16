# softwaredeisign-rpi-gps

## Server

```bash
# apt-get install python3-pip
# mkdir -p /var/www
# git clone https://github.com/y-egusa/softwaredeisign-rpi-gps.git /var/www/softwaredeisign-rpi-gps
# cd /var/www/softwaredeisign-rpi-gps/src
# pip3 install -r ../package.pip
# python3 manage.py migrate
# python3 manage.py loaddata ../initial.json
# sh ../bin/run.sh
```

Access to http://IPADDRESS:8000/

Superuser is `admin:test`.

THIS WAY IS INSECURE.
Set `DEBUG=False` and use the httpd (such as Nginx or Apache) to serve static files.

## Raspberry Pi

```bash
$ cd /home/pi
$ sudo apt-get install python3-pip
$ sudo pip-3.2 install pyserial
$ git clone https://github.com/y-egusa/softwaredeisign-rpi-gps.git
$ sh /home/pi/softwaredeisign-rpi-gps/rpi/run.sh
```
