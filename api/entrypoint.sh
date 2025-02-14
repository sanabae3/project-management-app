#!/bin/sh
# Exit on any error
set -e

# Run database migrations
flask db init || true
flask db migrate -m "Initial migration" || true
flask db upgrade

# Start Flask application using the correct entry point
exec gunicorn --bind :5000 --workers 1 --threads 4 run:app  # Use Gunicorn in production
