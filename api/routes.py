from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flask_cors import cross_origin  # ✅ Allow API calls from frontend
from models import db, User, Project, Task
import bcrypt

api_routes = Blueprint("api_routes", __name__)

@api_routes.route("/login", methods=["POST"])
@cross_origin()  # ✅ Allow frontend to call this endpoint
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    if user and bcrypt.checkpw(password.encode("utf-8"), user.password_hash.encode("utf-8")):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Invalid login credentials."}), 401

@api_routes.route("/users", methods=["GET"])
@jwt_required()
@cross_origin()
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "username": u.username} for u in users])

@api_routes.route("/projects", methods=["POST"])
@jwt_required()
@cross_origin()
def create_project():
    data = request.json
    current_user_id = get_jwt_identity()

    if not data.get("name"):
        return jsonify({"error": "Project name is required"}), 400

    try:
        project = Project(name=data["name"], owner_id=current_user_id)
        db.session.add(project)
        db.session.commit()
        return jsonify({"message": "Project created", "project_id": project.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@api_routes.route("/health", methods=["GET"])
@cross_origin()
def health_check():
    return jsonify(status="healthy"), 200
