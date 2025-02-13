from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db, User, Project, Task
import bcrypt  # Import bcrypt for password hashing

api_routes = Blueprint("api_routes", __name__)

@api_routes.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    if user and bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')): # Verify password
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Invalid login credentials."}), 401
    

# ✅ Fetch All Users
@api_routes.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "username": u.username} for u in users])

@api_routes.route("/projects", methods=["POST"])
@jwt_required()  # Protect the route - IMPORTANT!
def create_project():
    data = request.json
    current_user_id = get_jwt_identity()  # Get the logged-in user's ID

    if not data.get("project_name"):  # Validate project name (Important!)
        return jsonify({"error": "Project name is required"}), 400

    try:  # Add try-except block for better error handling
        project = Project(name=data["project_name"], owner_id=current_user_id)  # Use logged-in user's ID
        db.session.add(project)
        db.session.commit()
        return jsonify({"message": "Project created", "project_id": project.id}), 201  # Return project ID
    except Exception as e:  # Catch potential exceptions
        db.session.rollback()  # Rollback changes in case of error
        return jsonify({"error": str(e)}), 500  # Return error message and 500 status code

# ✅ Fetch All Tasks
@api_routes.route("/tasks", methods=["GET"])
@jwt_required()
def get_tasks():
    tasks = Task.query.all()
    return jsonify([
        {
            "id": t.id,
            "title": t.title,
            "project_id": t.project_id,
            "status": t.status
        } for t in tasks
    ])

# ✅ Create a Task
@api_routes.route("/tasks", methods=["POST"])
@jwt_required()
def create_task():
    data = request.json
    title = data.get("title")
    project_id = data.get("project_id")

    if not title or not project_id:
        return jsonify({"error": "Task title and project ID are required"}), 400

    new_task = Task(title=title, project_id=project_id)
    db.session.add(new_task)
    db.session.commit()

    return jsonify({"message": "Task created successfully"}), 201

# ✅ Update Task Status
@api_routes.route("/tasks/<int:task_id>/update", methods=["PUT"])
@jwt_required()
def update_task_status(task_id):
    task = Task.query.get(task_id)
    
    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.json
    task.status = data.get("status", "Completed")
    db.session.commit()

    return jsonify({"message": "Task status updated"}), 200
