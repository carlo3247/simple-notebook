#!/bin/bash

# Start Gunicorn process
echo Starting Gunicorn.
exec gunicorn team12scenario.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
