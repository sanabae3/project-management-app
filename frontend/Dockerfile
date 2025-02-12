# Use Nginx as a web server
FROM nginx:latest

# Create a non-root user (if it doesn't already exist in the base image)
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Copy website files into the Nginx container
COPY . /usr/share/nginx/html

# Create the cache directory and set ownership
RUN mkdir -p /var/cache/nginx/client_temp && \
    chown -R appuser:appuser /var/cache/nginx  # Change ownership to appuser

# Change file ownership to `appuser` for website files as well (Good practice)
RUN chown -R appuser:appuser /usr/share/nginx/html

# Switch to the appuser before copying nginx.conf
USER appuser

# Copy the modified nginx.conf file. Ensure the user directive is correct
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80 for HTTP traffic
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]