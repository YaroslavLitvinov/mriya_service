#!/bin/bash

#echo Current dir:
find /mriya_service -ls -type f

echo Start Nginx
/etc/init.d/nginx restart

# Start Gunicorn processes
exec gunicorn mriya_service.wsgi:application \
    --bind unix:/mriya_service.sock \
    --workers 3 \
    --log-file -
