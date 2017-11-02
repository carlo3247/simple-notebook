#!/bin/bash

NUM_WORKERS=3
TIMEOUT=120

# Start Gunicorn process
echo Starting Gunicorn.
exec gunicorn team12scenario.wsgi:application \
    --workers $NUM_WORKERS \
    --timeout $TIMEOUT \
    --bind 0.0.0.0:8000 \
