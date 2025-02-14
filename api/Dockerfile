# Use Python slim image
FROM python:3.9-slim-buster

# Set working directory
WORKDIR /app

# Create a non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Copy and install dependencies first (for better caching)
COPY requirements.txt /app/
RUN python3 -m venv /app/.venv && \
    /app/.venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Set file permissions
RUN chown -R appuser:appuser /app && chmod +x /app/entrypoint.sh

# Switch to non-root user
USER appuser

# Expose the application port
EXPOSE 5000

# Set environment variables for virtual environment activation
ENV PATH="/app/.venv/bin:$PATH"

# Run database migrations at runtime instead of build time
CMD ["sh", "-c", "flask db upgrade && /app/entrypoint.sh"]
