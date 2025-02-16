FROM nginx:latest

WORKDIR /usr/share/nginx/html

# Copy frontend files
COPY . .

# Copy custom NGINX configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80 for serving the frontend
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
