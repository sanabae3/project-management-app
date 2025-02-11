FROM python:3.9

WORKDIR /app

COPY . /app

# Create a non-root user and group
RUN addgroup -S appuser && adduser -S -G appuser appuser

# Switch to the non-root user
USER appuser

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN flask db init
COPY migrations /app/migrations
RUN flask db upgrade

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

EXPOSE 5000

ENV API_PORT=${API_PORT}
ENV FLASK_DEBUG=1 # Or True

CMD ["/app/entrypoint.sh"]