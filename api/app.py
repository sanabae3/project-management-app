from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from models import db
from routes import api_routes

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config.from_object("config.Config")

# Enable CORS for frontend communication
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Initialize Database
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# ✅ Register API routes under `/api`
app.register_blueprint(api_routes, url_prefix="/api")

# ✅ Health check for debugging
@app.route("/health", methods=["GET"])
def root_health_check():
    return {"status": "healthy (root)"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("API_PORT", 5000)), debug=False)
