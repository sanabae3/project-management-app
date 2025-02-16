#!/bin/bash
set -e

# Ensure logs are visible in Docker logs
exec gunicorn --bind 0.0.0.0:5000 --workers 3 --threads 4 --access-logfile - --error-logfile - run:app
