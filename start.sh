#!/bin/bash

echo Apply database migrations
python manage.py makemigrations mriya_service

#echo Current dir:
#exec find . -type f
#echo project dir:
#exec find /docker_mriya -type f

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn mriya_service.wsgi:application \
    --bind 0.0.0.0:80 \
    --workers 3
