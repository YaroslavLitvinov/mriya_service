#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
#echo Current dir:
#exec find . -type f
#echo project dir:
#exec find /docker_mriya -type f
exec gunicorn mriya_service.wsgi:application \
    --bind 0.0.0.0:80 \
    --workers 3
