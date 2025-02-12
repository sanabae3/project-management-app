# Multi-stage build
FROM python:3.9-slim-buster AS builders

WORKDIR /app

COPY . /app

# ✅ Install dependencies as root before switching to appuser
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Create non-root user and group (For build stage)
RUN groupadd -r appuser && useradd -r -g appuser appuser
USER appuser

# ✅ Ensure appuser has access to the application directory
RUN chown -R appuser:appuser /app

# ✅ Run Flask Migrations (now as appuser)
RUN flask db init || true  # Allow failure if already initialized
RUN flask db migrate -m "Initial migration" || true
RUN flask db upgrade || true

# Final stage
FROM python:3.9-slim-buster

# ✅ Create the user again in the final stage
RUN groupadd -r appuser && useradd -r -g appuser appuser

# COPY from builder stage
COPY --from=builders /app /app

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

WORKDIR /app
USER appuser  # ✅ Now this user exists in the final image

EXPOSE 5000

ENV API_PORT=${API_PORT}
ENV FLASK_DEBUG=1

CMD ["/app/entrypoint.sh"]
