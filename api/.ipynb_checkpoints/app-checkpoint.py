from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os
from models import db
from routes import api_routes
from config import Config

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

# Initialize Database
db.init_app(app)

# Enable JWT Authentication
jwt = JWTManager(app)

# Register API routes
app.register_blueprint(api_routes)

# Run the app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensure tables exist
    app.run(host="0.0.0.0", port=int(os.getenv("API_PORT")), debug=True)
