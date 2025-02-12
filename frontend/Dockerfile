# Use Nginx as a web server
FROM nginx:latest

# Create a non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Copy website files into the Nginx container
COPY . /usr/share/nginx/html

# Change file ownership to `appuser`
RUN chown -R appuser:appuser /usr/share/nginx/html

# Set the non-root user for running Nginx
USER appuser

# Expose port 80 for HTTP traffic
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
