#!/bin/bash

NUM_WORKERS=3
TIMEOUT=120

# Start Gunicorn process
echo Starting Gunicorn.
exec gunicorn team12scenario.wsgi:application \
    --workers $NUM_WORKERS \
    --timeout $TIMEOUT \
    --bind 0.0.0.0:8000 \



    docker ps -q -a | xargs docker rm
    docker build -t djangoapp:$BUILD_NUMBER .
    docker run -p 8000:8000 djangoapp:$BUILD_NUMBER &
