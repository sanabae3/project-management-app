# Builder stage
FROM python:3.9-slim-buster AS builders

WORKDIR /app

# Create and activate the virtual environment
RUN python3 -m venv .venv
RUN . .venv/bin/activate  # Or RUN bash -c "source .venv/bin/activate"

# Copy requirements *before* installing (for better caching)
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

# List installed packages (for debugging)
RUN pip freeze > /app/installed_packages.txt
COPY installed_packages.txt /app/

COPY . /app  # Copy the rest of the application code

# Create non-root user and group
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Run Flask Migrations (as appuser) - Important: Switch user *before* migrations
USER appuser
RUN flask db init || true
RUN flask db migrate -m "Initial migration" || true
RUN flask db upgrade || true


# Final stage
FROM python:3.9-slim-buster

# Create the appuser in the final stage
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Copy the virtual environment (THIS IS THE KEY CHANGE)
COPY --from=builders /app/.venv /app/.venv

# Copy app code
COPY --from=builders /app /app

COPY entrypoint.sh /app/entrypoint.sh
RUN chown appuser:appuser /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

USER appuser

WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["/app/entrypoint.sh"]