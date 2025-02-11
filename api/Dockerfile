# Use Python base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Ensure pip is up to date
RUN pip install --upgrade pip

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Expose Flask's API port (from .env)
EXPOSE ${API_PORT}

# Run entrypoint script automatically
ENTRYPOINT ["sh", "/app/entrypoint.sh"]
