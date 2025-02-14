import os
from dotenv import load_dotenv

# Load environment variables FIRST (Crucial!)
load_dotenv()  # This MUST be before any other imports

from app import app  # Now app.py will have access to the env vars

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("API_PORT", 5000)), debug=True)  # Get port from env