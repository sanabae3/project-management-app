from flask import Blueprint, request, jsonify
from models import db, User, Project, Task

api_routes = Blueprint("api_routes", __name__)

@api_routes.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"user_id": u.user_id, "username": u.username} for u in users])

@api_routes.route("/projects", methods=["POST"])
def create_project():
    data = request.json
    project = Project(project_name=data["project_name"], created_by=1)
    db.session.add(project)
    db.session.commit()
    return jsonify({"message": "Project created"}), 201

@api_routes.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    task = Task(task_name=data["task_name"], project_id=data["project_id"], assigned_to=data["assigned_to"])
    db.session.add(task)
    db.session.commit()
    return jsonify({"message": "Task created"}), 201

# ✅ Fetch All Tasks
@api_routes.route("/tasks", methods=["GET"])
@jwt_required()
def get_tasks():
    tasks = Task.query.all()
    return jsonify([
        {
            "task_id": t.task_id,
            "task_name": t.task_name,
            "project_id": t.project_id,
            "assigned_to": t.assigned_to,
            "status": t.status
        } for t in tasks
    ])

# ✅ Create a Task
@api_routes.route("/tasks", methods=["POST"])
@jwt_required()
def create_task():
    data = request.json
    task_name = data.get("task_name")
    project_id = data.get("project_id")

    if not task_name or not project_id:
        return jsonify({"error": "Task name and project ID are required"}), 400

    new_task = Task(task_name=task_name, project_id=project_id)
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

    task.status = "Completed"
    db.session.commit()

    return jsonify({"message": "Task marked as completed"}), 200

