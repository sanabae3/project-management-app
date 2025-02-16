FROM mysql:latest

# Set environment variables
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=project_management
ENV MYSQL_USER=app_user
ENV MYSQL_PASSWORD=Password1

# Copy custom MySQL configuration
COPY my.cnf /etc/mysql/my.cnf

# Copy initialization SQL script
COPY init.sql /docker-entrypoint-initdb.d/

# Expose MySQL port
EXPOSE 3306
