# Builder stage
FROM python:3.9-slim-buster AS builders

WORKDIR /app

# Create and activate the virtual environment (Recommended)
RUN python3 -m venv .venv
RUN source .venv/bin/activate

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

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

# Copy the virtual environment (Key change - Copy installed packages)
COPY --from=builders /app/.venv /app/.venv 
# Copy app code
COPY --from=builders /app /app

USER appuser

COPY entrypoint.sh /app/entrypoint.sh
RUN chown appuser:appuser /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["/app/entrypoint.sh"]