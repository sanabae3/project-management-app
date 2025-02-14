CREATE DATABASE IF NOT EXISTS project_management;
USE project_management;

-- Create the application user (app_user)
CREATE USER IF NOT EXISTS 'app_user'@'%' IDENTIFIED BY 'P@$$wOrd'; -- Replace with your password
GRANT SELECT, INSERT, UPDATE, DELETE ON project_management.* TO 'app_user'@'%';
FLUSH PRIVILEGES;

CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    description TEXT,
    created_by INT NOT NULL,
    FOREIGN KEY (created_by) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    task_name VARCHAR(255) NOT NULL,
    description TEXT,
    project_id INT NOT NULL,
    assigned_to INT,
    status ENUM('Pending', 'In Progress', 'Completed') NOT NULL DEFAULT 'Pending',
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (assigned_to) REFERENCES users(user_id) ON DELETE SET NULL
);

-- Insert the initial user (admin user)
INSERT INTO users (username, email, password_hash)
VALUES ('admin', 'admin@example.com', '$2b$12$dzstnd.SoHX0ED3WvQUIGu8/BsMnD47FifeWYzioGnsho/b6sTmBO'); -- Replace with the bcrypt hash

-- Or if you are not using bcrypt hash for the initial user. 
-- INSERT INTO users (username, email, password_hash)
-- VALUES ('admin', 'admin@example.com', 'admin_password'); -- Replace with a strong and secure password.