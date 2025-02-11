from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate  # ✅ Import Flask-Migrate
from dotenv import load_dotenv
import os
from models import db  # Import db instance from models
from routes import api_routes
from config import Config

# Load environment variables from .env
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Database
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)  # ✅ Add Flask-Migrate for `flask db` commands

# Enable JWT Authentication
jwt = JWTManager(app)

# Register API routes
app.register_blueprint(api_routes)

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("API_PORT", 5000)), debug=False)
