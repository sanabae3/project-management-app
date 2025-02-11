# Use Python base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Copy .env file explicitly (important for runtime)
COPY .env /app/.env

# Ensure pip is up to date
RUN pip install --upgrade pip

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Expose Flask's API port
EXPOSE 5000

# Set environment variables from .env (if needed)
ENV API_PORT=${API_PORT}

# Run entrypoint script automatically
ENTRYPOINT ["sh", "/app/entrypoint.sh"]
