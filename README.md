# project-management-app
Here’s a **summarized `README.md`** file that provides clear instructions on setting up and running the project.

---

## **📌 Project Management App**
A **containerized** Project Management App with a **Flask API, MySQL database, and an NGINX frontend**.

### **📁 Project Structure**
```
project-management-app/
│── api/                 # Flask API (Backend)
│── frontend/            # Static Frontend (HTML, CSS, JS)
│── database/            # MySQL Database Setup
│── docker-compose.yml   # Docker Services Configuration
│── .env                 # Environment Variables
│── README.md            # Documentation
```

---

## **🚀 Getting Started**
### **1️⃣ Prerequisites**
Ensure you have **Docker & Docker Compose** installed:
```sh
docker --version
docker compose version
```

### **2️⃣ Clone the Repository**
```sh
git clone https://github.com/your-repo/project-management-app.git
cd project-management-app
```

### **3️⃣ Set Up Environment Variables**
Modify the `.env` file as needed:
```ini
API_PORT=5000
FRONTEND_PORT=80
DATABASE_USER=app_user
DATABASE_PASSWORD=Password1
DATABASE_NAME=project_management
MYSQL_ROOT_PASSWORD=root
DATABASE_HOST=database
DATABASE_URL=mysql+pymysql://app_user:Password1@database/project_management
```

### **4️⃣ Build & Start the Containers**
```sh
docker compose up -d --build
```

### **5️⃣ Verify Services**
Check running containers:
```sh
docker ps
```
View logs:
```sh
docker logs project-management-api
```

---

## **🔗 Access the Application**
| Service   | URL |
|-----------|----------------------------------|
| **Frontend** | `http://localhost:80` |
| **API**      | `http://localhost:5000` |
| **Database** | Connect via MySQL client |

---

## **📂 API Endpoints**
### **🔐 Authentication**
- `POST /login` → Authenticate and get JWT Token
- `POST /register` → Register a new user

### **📁 Projects**
- `GET /projects` → List all projects
- `POST /projects` → Create a new project
- `DELETE /projects/{id}` → Delete a project

### **📌 Tasks**
- `GET /tasks` → List all tasks
- `POST /tasks` → Create a new task
- `PUT /tasks/{id}/update` → Update task status

---

## **🐞 Troubleshooting**
| Issue | Solution |
|-------|----------|
| MySQL container fails to start | Run `docker compose down -v` and restart |
| API cannot connect to database | Ensure `DATABASE_HOST=database` in `.env` |
| Frontend does not load | Ensure `FRONTEND_PORT=80` is mapped correctly |

---

## **📜 License**
This project is **MIT Licensed**. Feel free to use and modify!

🚀 **Happy Coding!** 🚀