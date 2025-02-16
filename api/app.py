from flask import Flask, jsonify
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

# ✅ Load configuration from `config.py`
app.config.from_object("config.Config")

# ✅ Enable CORS to allow frontend to access API
CORS(app, resources={r"/api/*": {"origins": "*"}})

# ✅ Initialize Database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# ✅ Initialize JWT authentication
jwt = JWTManager(app)

# ✅ Import & register routes
from routes import api_routes
app.register_blueprint(api_routes, url_prefix="/api")

# ✅ Health check route
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200

# ✅ Run the app when executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("API_PORT", 5000)), debug=False)
