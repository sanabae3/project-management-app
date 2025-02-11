from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db, User, Project, Task

api_routes = Blueprint("api_routes", __name__)

# ✅ Fetch All Users
@api_routes.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "username": u.username} for u in users])

# ✅ Create a Project
@api_routes.route("/projects", methods=["POST"])
def create_project():
    data = request.json
    project = Project(name=data["project_name"], owner_id=data["created_by"])
    db.session.add(project)
    db.session.commit()
    return jsonify({"message": "Project created"}), 201

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
