# Builder stage (for dependencies and migrations)
FROM python:3.9-slim-buster AS builders

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app  

# Create non-root user and group
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Run Flask Migrations (as appuser) - Important: Switch user *before* migrations
USER appuser
RUN flask db init || true  # Allow failure if already initialized
RUN flask db migrate -m "Initial migration" || true
RUN flask db upgrade || true


FROM python:3.9-slim-buster

# Create a non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set working directory
WORKDIR /app

# Copy and set ownership in one step
COPY --chown=appuser:appuser entrypoint.sh /app/entrypoint.sh

# Ensure the script is executable
RUN chmod +x /app/entrypoint.sh

# Switch to non-root user
USER appuser

# Expose the port (if needed)
EXPOSE 5000

# Define the entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
