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


# Final stage (for running the app)
FROM python:3.9-slim-buster

# Create the appuser in the final stage (This is the crucial change)
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Copy from builder stage
COPY --from=builders /app /app

# Switch to the non-root user *before* copying entrypoint.sh
USER appuser

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Set the working directory
WORKDIR /app

# Expose the port (if needed) - should also be in docker-compose
EXPOSE 5000 

# Define the ENTRYPOINT (using exec)
ENTRYPOINT ["/app/entrypoint.sh"]