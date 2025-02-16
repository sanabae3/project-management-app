FROM python:3.9

WORKDIR /app

# Copy project files
COPY . /app

# Create a virtual environment and activate it
RUN python -m venv .venv
RUN . .venv/bin/activate

# Upgrade pip
RUN pip install --upgrade pip

# Ensure dependencies including PyMySQL are installed
RUN pip install -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Set the entrypoint script
ENTRYPOINT ["/bin/bash", "entrypoint.sh"]
