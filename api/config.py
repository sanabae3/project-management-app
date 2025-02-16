import os
from dotenv import load_dotenv
import secrets

# Load environment variables
load_dotenv()

# Generate secure keys if not set
SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_hex(32))
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", secrets.token_hex(32))
PASSWORD_HASH_SALT = os.getenv("PASSWORD_HASH_SALT", secrets.token_hex(16))

class Config:
    # Flask Configuration
    FLASK_APP = os.getenv("FLASK_APP", "run.py")
    FLASK_ENV = os.getenv("FLASK_ENV", "production")
    API_PORT = int(os.getenv("API_PORT", 5000))
    
    # Security Configuration
    SECRET_KEY = SECRET_KEY
    JWT_SECRET_KEY = JWT_SECRET_KEY
    PASSWORD_HASH_SALT = PASSWORD_HASH_SALT
    
    # Database Configuration (Use pymysql explicitly)
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", 'mysql+pymysql://app_user:Password1@db/project_management')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # AWS Configuration (If needed)
    AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", "")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "")
    AWS_SSH_KEY_NAME = os.getenv("AWS_SSH_KEY_NAME", "my-aws-key")
    
    # Docker Configuration
    DOCKER_NETWORK = os.getenv("DOCKER_NETWORK", "project_network")
