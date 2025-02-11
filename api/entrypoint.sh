#!/bin/sh
# Exit on any error
set -e

# Install dependencies (ensures latest versions)
pip install --no-cache-dir -r requirements.txt

# Run database migrations (if needed)
if flask db upgrade; then
    echo "Database migrations applied."
else
    echo "No migrations found or database not initialized."
fi

# Start Flask application using the correct entry point
exec python run.py
