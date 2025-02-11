#!/bin/sh

# Run database migrations (if needed) - Better approach
if flask db upgrade; then
    echo "Database migrations applied."
elif [ "$?" -eq 1 ]; then # Check exit code specifically for flask db upgrade
    echo "Database migrations failed. Check logs."
    exit 1 # Exit with error code if migrations fail
else
    echo "No migrations found or database already up-to-date." # More accurate message
fi

exec gunicorn --bind 0.0.0.0:$API_PORT --workers 4 --threads 4 app:app