# Multi-stage build
FROM python:3.9-slim-buster AS builders

WORKDIR /app

COPY . /app

# Create non-root user and group
RUN groupadd -r appuser && useradd -r -g appuser appuser
USER appuser

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Migrations (Starting from scratch)
RUN flask db init
RUN flask db migrate -m "Initial migration"
RUN flask db upgrade

# Final stage
FROM python:3.9-slim-buster

# COPY from builder stage (ownership is preserved)
COPY --from=builders /app /app  # Simplified path

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

EXPOSE 5000

ENV API_PORT=${API_PORT}
ENV FLASK_DEBUG=1

CMD ["/app/entrypoint.sh"]