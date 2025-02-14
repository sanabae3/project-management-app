#!/bin/sh
set -e

source /app/.venv/bin/activate

exec gunicorn --bind :5000 --workers 1 --threads 4 run:app