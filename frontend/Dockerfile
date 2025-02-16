# Use official NGINX image
FROM nginx:latest

# Set working directory
WORKDIR /usr/share/nginx/html

# Copy website files to NGINX directory
COPY . /usr/share/nginx/html

# Copy custom NGINX configuration
COPY nginx.conf /etc/nginx/nginx.conf

# ✅ Fix file permissions for NGINX
RUN chmod -R 755 /usr/share/nginx/html && \
    chown -R nginx:nginx /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start NGINX
CMD ["nginx", "-g", "daemon off;"]
