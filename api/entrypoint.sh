#!/bin/sh
# Exit on any error
set -e

# Start Flask application using the correct entry point
exec gunicorn --bind :5000 --workers 1 --threads 4 run:app  # Use Gunicorn in production
# OR (for development/debugging only)
# exec python run.py