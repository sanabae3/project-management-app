import pymysql
pymysql.install_as_MySQLdb()  # ✅ Enforce pymysql for SQLAlchemy

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS  # ✅ Enable CORS
from dotenv import load_dotenv
import os
from models import db
from routes import api_routes
from config import Config

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Enable CORS for frontend communication
CORS(app, resources={r"/api/*": {"origins": "*"}})  # ✅ Allow frontend to call API

# Initialize Database
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Enable JWT Authentication
jwt = JWTManager(app)

# Register API routes under /api/
app.register_blueprint(api_routes, url_prefix="/api")  # ✅ Consistent API prefix

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("API_PORT", 5000)), debug=False)
