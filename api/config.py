import os
from dotenv import load_dotenv
import secrets

load_dotenv()  # Load .env file

# Generate secure keys if not set (Important: Keep these)
SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_hex(32))
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", secrets.token_hex(32))
PASSWORD_HASH_SALT = os.getenv("PASSWORD_HASH_SALT", secrets.token_hex(16))

class Config:
    # Flask configuration
    FLASK_APP = os.getenv("FLASK_APP", "run.py")
    FLASK_ENV = os.getenv("FLASK_ENV", "production")
    API_PORT = int(os.getenv("API_PORT", 5000))
    
    # Security configuration (Use the generated keys)
    SECRET_KEY = SECRET_KEY
    JWT_SECRET_KEY = JWT_SECRET_KEY
    PASSWORD_HASH_SALT = PASSWORD_HASH_SALT
    
    # Database configuration (Use the single DATABASE_URL)
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")  # Crucial change!
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # CORS configuration
    CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "http://localhost")
    
    # AWS configuration (Keep these if needed)
    AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", "")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "")
    AWS_SSH_KEY_NAME = os.getenv("AWS_SSH_KEY_NAME", "my-aws-key")
    
    # Docker configuration (Keep this if needed)
    DOCKER_NETWORK = os.getenv("DOCKER_NETWORK", "project_network")