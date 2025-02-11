import os
from dotenv import load_dotenv
import secrets

# Load environment variables from .env
load_dotenv()

# Generate secure keys if not set
SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_hex(32))
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", secrets.token_hex(32))
PASSWORD_HASH_SALT = os.getenv("PASSWORD_HASH_SALT", secrets.token_hex(16))

class Config:
    # Flask configuration
    FLASK_APP = os.getenv("FLASK_APP", "app.py")
    FLASK_ENV = os.getenv("FLASK_ENV", "production")
    API_PORT = int(os.getenv("API_PORT", 5000))
    
    # Security configuration
    SECRET_KEY = SECRET_KEY
    JWT_SECRET_KEY = JWT_SECRET_KEY
    PASSWORD_HASH_SALT = PASSWORD_HASH_SALT
    
    # Database configuration
    DATABASE_HOST = os.getenv("DATABASE_HOST", "db")
    DATABASE_PORT = int(os.getenv("DATABASE_PORT", 3306))
    DATABASE_NAME = os.getenv("DATABASE_NAME", "project_management")
    DATABASE_USER = os.getenv("DATABASE_USER", "root")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "root")
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # CORS configuration
    CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "http://localhost")
    
    # AWS configuration
    AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", "")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "")
    AWS_SSH_KEY_NAME = os.getenv("AWS_SSH_KEY_NAME", "my-aws-key")
    
    # Docker configuration
    DOCKER_NETWORK = os.getenv("DOCKER_NETWORK", "project_network")
