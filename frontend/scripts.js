// API Base URL
const API_BASE_URL = "http://18.224.66.241:5000"; // ✅ Use the Docker service name

// Function to check if user is logged in
function checkAuth() {
    const token = getToken();
    if (!token) {
        window.location.href = "login.html";
    }
}

// Function to log out user
function logout() {
    localStorage.removeItem("token");
    window.location.href = "login.html";
}

// Function to get JWT Token from local storage
function getToken() {
    return localStorage.getItem("token");
}

// ✅ Function to handle user login
async function loginUser(event) {
    event.preventDefault();
    
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const errorMessage = document.getElementById("errorMessage");
    const loginButton = document.getElementById("loginButton");
    const loading = document.getElementById("loading");

    // Reset UI
    errorMessage.textContent = "";
    loading.classList.remove("hidden");
    loginButton.disabled = true;

    try {
        const response = await fetch(`${API_BASE_URL}/login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();

        if (response.ok) {
            localStorage.setItem("token", data.access_token);
            window.location.href = "index.html"; 
        } else {
            throw new Error(data.error || "Invalid login credentials.");
        }
    } catch (error) {
        errorMessage.textContent = error.message;
    } finally {
        loginButton.disabled = false;
        loading.classList.add("hidden");
    }
}

// ✅ Function to fetch and display dashboard stats
async function fetchDashboard() {
    checkAuth();

    const errorMessage = document.getElementById("errorMessage");
    const loading = document.getElementById("loading");

    loading.classList.remove("hidden");
    errorMessage.classList.add("hidden");

    try {
        const response = await fetch(`${API_BASE_URL}/dashboard`, {
            headers: {
                "Authorization": `Bearer ${getToken()}`,
                "Content-Type": "application/json"
            }
        });

        if (!response.ok) throw new Error("Failed to fetch dashboard data.");

        const data = await response.json();
        document.getElementById("totalUsers").innerText = data.total_users;
        document.getElementById("totalProjects").innerText = data.total_projects;
        document.getElementById("totalTasks").innerText = data.total_tasks;
        document.getElementById("completedTasks").innerText = data.completed_tasks;
    } catch (error) {
        errorMessage.textContent = error.message;
        errorMessage.classList.remove("hidden");
    } finally {
        loading.classList.add("hidden");
    }
}

// ✅ Function to load projects
async function loadProjects() {
    checkAuth();

    const response = await fetch(`${API_BASE_URL}/projects`, {
        headers: { "Authorization": `Bearer ${getToken()}` }
    });

    const data = await response.json();
    const projectList = document.getElementById("projectList");
    const taskProject = document.getElementById("taskProject");

    projectList.innerHTML = "";
    taskProject.innerHTML = "";

    data.forEach(project => {
        const li = document.createElement("li");
        li.innerText = project.name;
        projectList.appendChild(li);

        const option = document.createElement("option");
        option.value = project.id;
        option.innerText = project.name;
        taskProject.appendChild(option);
    });
}

// ✅ Function to create a project
async function createProject(event) {
    event.preventDefault();

    const projectName = document.getElementById("projectName").value;

    const response = await fetch(`${API_BASE_URL}/projects`, {
        method: "POST",
        headers: {
            "Authorization": `Bearer ${getToken()}`,
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name: projectName })
    });

    if (response.ok) {
        loadProjects();
        document.getElementById("projectForm").reset();
    } else {
        alert("Failed to create project.");
    }
}

// ✅ Function to create a task
async function createTask(event) {
    event.preventDefault();

    const taskName = document.getElementById("taskName").value;
    const projectId = document.getElementById("taskProject").value;

    const response = await fetch(`${API_BASE_URL}/tasks`, {
        method: "POST",
        headers: {
            "Authorization": `Bearer ${getToken()}`,
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ title: taskName, project_id: projectId })
    });

    if (response.ok) {
        loadTasks();
        document.getElementById("taskForm").reset();
    } else {
        alert("Failed to create task.");
    }
}

// ✅ Function to update task status
async function updateTaskStatus(taskId) {
    const response = await fetch(`${API_BASE_URL}/tasks/${taskId}/update`, {
        method: "PUT",
        headers: {
            "Authorization": `Bearer ${getToken()}`,
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ status: "Completed" })
    });

    if (response.ok) {
        loadTasks();
    } else {
        alert("Failed to update task.");
    }
}

// ✅ Attach event listeners on page load
document.addEventListener("DOMContentLoaded", () => {
    if (document.getElementById("loginForm")) {
        document.getElementById("loginForm").addEventListener("submit", loginUser);
    }
    if (document.getElementById("projectForm")) {
        document.getElementById("projectForm").addEventListener("submit", createProject);
        loadProjects();
    }
    if (document.getElementById("taskForm")) {
        document.getElementById("taskForm").addEventListener("submit", createTask);
        loadTasks();
    }
    if (document.getElementById("totalUsers")) {
        fetchDashboard();
    }
    
    // ✅ Password Visibility Toggle
    const passwordField = document.getElementById("password");
    const togglePassword = document.getElementById("togglePassword");

    if (togglePassword) {
        togglePassword.addEventListener("click", () => {
            passwordField.type = passwordField.type === "password" ? "text" : "password";
            togglePassword.textContent = passwordField.type === "password" ? "👁️" : "🙈";
        });
    }
});

async function loadTasks() {
    checkAuth();
    const response = await fetch(`${API_BASE_URL}/tasks`, {
        headers: { "Authorization": `Bearer ${getToken()}` }
    });
    const data = await response.json();
    const taskList = document.getElementById("taskList"); // Make sure you have this element in your HTML

    taskList.innerHTML = ""; // Clear existing tasks

    data.forEach(task => {
        const li = document.createElement("li");
        li.innerHTML = `${task.title} - ${task.status} <button onclick="updateTaskStatus(${task.id})">Complete</button>`; // Add complete button
        taskList.appendChild(li);
    });
}