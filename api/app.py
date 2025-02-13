from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from models import db
from routes import api_routes
from config import Config
from flask_cors import CORS  # Import CORS

# Load environment variables from .env
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# CORS Configuration (Enable CORS for all routes - adjust origins in production!)
CORS(app)  # Or CORS(app, origins=["your-frontend-domain"]) for production

# Initialize Database
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Enable JWT Authentication
jwt = JWTManager(app)

# Register API routes
app.register_blueprint(api_routes)

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("API_PORT", 5000)), debug=False)