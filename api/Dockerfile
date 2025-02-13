# Builder stage
FROM python:3.9-slim-buster AS builders

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt  # Install as root (OK in builder stage)

COPY . /app

# Create non-root user and group
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Run Flask Migrations (as appuser)
USER appuser
RUN flask db init || true
RUN flask db migrate -m "Initial migration" || true
RUN flask db upgrade || true

# Final stage
FROM python:3.9-slim-buster

# Create the appuser in the final stage (Crucial for permissions)
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Copy installed packages from the builder stage (THIS IS THE KEY CHANGE)
COPY --from=builders /app/venv /app/venv  
COPY --from=builders /app/.local /app/.local 

# Copy app code
COPY --from=builders /app /app

USER appuser

COPY entrypoint.sh /app/entrypoint.sh
RUN chown appuser:appuser /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["/app/entrypoint.sh"]