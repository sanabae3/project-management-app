#!/bin/sh
# Exit on any error
set -e

# Initialize the migrations directory if it doesn't exist
if [ ! -d "/app/migrations" ]; then
    flask db init
fi

# Create an initial migration if none exists
if [ -z "$(ls -A /app/migrations/versions)" ]; then
    flask db migrate -m "Initial migration"
fi

# Apply the migrations
flask db upgrade

# Start Flask application using the correct entry point
exec gunicorn --bind :5000 --workers 1 --threads 4 run:app  # Use Gunicorn in production
