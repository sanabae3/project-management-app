FROM nginx:latest

RUN groupadd -r appuser && useradd -r -g appuser appuser

COPY . /usr/share/nginx/html

RUN mkdir -p /var/cache/nginx/client_temp && \
    chown -R appuser:appuser /var/cache/nginx /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
