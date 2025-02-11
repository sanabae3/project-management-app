# Use Nginx as a web server
FROM nginx:latest

# Copy website files into the Nginx container
COPY . /usr/share/nginx/html

# Expose port 80 for HTTP traffic
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
