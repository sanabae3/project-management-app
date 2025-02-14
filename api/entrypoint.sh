#!/bin/bash
set -e

# Activate the virtual environment
source /app/.venv/bin/activate

# Start Flask application using Gunicorn
exec gunicorn --bind :5000 --workers 1 --threads 4 run:app
