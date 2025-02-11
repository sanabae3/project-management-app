CREATE DATABASE IF NOT EXISTS project_management;
USE project_management;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL  -- Increased length for hashed passwords
);

CREATE TABLE projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    created_by INT NOT NULL,
    FOREIGN KEY (created_by) REFERENCES users(user_id) ON DELETE CASCADE  -- Ensures projects are deleted if user is removed
);

CREATE TABLE tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    task_name VARCHAR(255) NOT NULL,
    project_id INT NOT NULL,
    assigned_to INT,
    status ENUM('Pending', 'In Progress', 'Completed') NOT NULL DEFAULT 'Pending',  -- Ensures status is always set
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,  -- Deletes tasks if project is deleted
    FOREIGN KEY (assigned_to) REFERENCES users(user_id) ON DELETE SET NULL  -- If user is deleted, assigned tasks become unassigned
);
