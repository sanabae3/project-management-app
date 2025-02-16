from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Load configuration
app.config.from_object("config.Config")

# Enable CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Initialize Database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize JWT authentication
jwt = JWTManager(app)

# Import & register routes
from routes import api_routes
app.register_blueprint(api_routes, url_prefix="/api")

# ✅ Default route should redirect to login page
@app.route("/")
def home():
    return redirect(url_for("login"))

# ✅ Render login page
@app.route("/login")
def login():
    return render_template("login.html")

# ✅ Health check route
@app.route("/health", methods=["GET"])
def health_check():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("API_PORT", 5000)), debug=False)
