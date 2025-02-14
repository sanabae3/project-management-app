# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash # Import security functions
# # Initialize SQLAlchemy
# db = SQLAlchemy()

# # User Model
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     password_hash = db.Column(db.String(255), nullable=False)

#     # Relationship to projects
#     projects = db.relationship("Project", backref="owner", lazy=True, cascade="all, delete")

#     def __repr__(self):
#         return f"<User {self.username}>"

# # Project Model
# class Project(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.Text, nullable=True)
#     owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

#     # Relationship to tasks
#     tasks = db.relationship("Task", backref="project", lazy=True, cascade="all, delete")

#     def __repr__(self):
#         return f"<Project {self.name}>"

# # Task Model
# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.Text, nullable=True)
#     status = db.Column(db.String(20), nullable=False, default="Pending")
#     project_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False)

#     def __repr__(self):
#         return f"<Task {self.title} - {self.status}>"

# class User(db.Model):
#     # ... (other columns)
#     password_hash = db.Column(db.String(255), nullable=False)

#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize SQLAlchemy
db = SQLAlchemy()

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    # Relationship to projects
    projects = db.relationship("Project", backref="owner", lazy=True, cascade="all, delete")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
       return f"<User {self.username}>"

# Project Model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    # Relationship to tasks
    tasks = db.relationship("Task", backref="project", lazy=True, cascade="all, delete")

    def __repr__(self):
        return f"<Project {self.name}>"

# Task Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), nullable=False, default="Pending")
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False)

    def __repr__(self):
        return f"<Task {self.title} - {self.status}>"