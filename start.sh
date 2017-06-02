#!/bin/bash

echo /var/www dir:
find /var/www -ls -type f

echo PYTHONPATH $PYTHONPATH

echo Start Nginx
/etc/init.d/nginx restart

# Start Gunicorn processes
exec gunicorn mriya_service.wsgi:application \
    --bind unix:/mriya_service.sock \
    --workers 3 \
    --log-file -
