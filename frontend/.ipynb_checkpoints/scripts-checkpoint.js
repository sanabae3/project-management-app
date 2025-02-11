// API Base URL (Modify this if needed)
const API_BASE_URL = "http://localhost:5000";

// Function to check if user is logged in
function checkAuth() {
    const token = localStorage.getItem("token");
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

// Function to handle user login
async function loginUser(event) {
    event.preventDefault();
    
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch(`${API_BASE_URL}/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
    });

    const data = await response.json();

    if (response.ok) {
        localStorage.setItem("token", data.token);
        window.location.href = "index.html"; // Redirect to main dashboard
    } else {
        document.getElementById("errorMessage").innerText = data.error;
    }
}

// Function to fetch and display dashboard stats
async function loadDashboard() {
    checkAuth();
    
    const response = await fetch(`${API_BASE_URL}/dashboard`, {
        headers: { "Authorization": `Bearer ${getToken()}` }
    });

    const data = await response.json();
    document.getElementById("totalUsers").innerText = data.total_users;
    document.getElementById("totalProjects").innerText = data.total_projects;
    document.getElementById("totalTasks").innerText = data.total_tasks;
    document.getElementById("completedTasks").innerText = data.completed_tasks;
}

// Function to load projects
async function loadProjects() {
    checkAuth();

    const response = await fetch(`${API_BASE_URL}/projects`, {
        headers: { "Authorization": `Bearer ${getToken()}` }
    });

    const data = await response.json();
    const projectList = document.getElementById("projectList");
    projectList.innerHTML = "";

    data.forEach(project => {
        const li = document.createElement("li");
        li.innerText = project.project_name;
        projectList.appendChild(li);
    });
}

// Function to create a project
async function createProject(event) {
    event.preventDefault();

    const projectName = document.getElementById("projectName").value;

    const response = await fetch(`${API_BASE_URL}/projects`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${getToken()}`
        },
        body: JSON.stringify({ project_name: projectName })
    });

    if (response.ok) {
        loadProjects();
        document.getElementById("projectForm").reset();
    } else {
        alert("Failed to create project");
    }
}

// Attach event listeners
document.addEventListener("DOMContentLoaded", () => {
    if (document.getElementById("loginForm")) {
        document.getElementById("loginForm").addEventListener("submit", loginUser);
    }
    if (document.getElementById("projectForm")) {
        document.getElementById("projectForm").addEventListener("submit", createProject);
        loadProjects();
    }
    if (document.getElementById("totalUsers")) {
        loadDashboard();
    }
});

// ✅ Fetch & Display Tasks
async function loadTasks() {
    checkAuth();
    const response = await fetch(`${API_BASE_URL}/tasks`, {
        headers: { "Authorization": `Bearer ${getToken()}` }
    });

    const data = await response.json();
    const taskList = document.getElementById("taskList");
    taskList.innerHTML = "";

    data.forEach(task => {
        const li = document.createElement("li");
        li.innerHTML = `
            ${task.task_name} - ${task.status} 
            <button onclick="updateTaskStatus(${task.task_id})">Mark as Completed</button>
        `;
        taskList.appendChild(li);
    });
}

// ✅ Create a Task
async function createTask(event) {
    event.preventDefault();

    const taskName = document.getElementById("taskName").value;
    const projectId = document.getElementById("taskProject").value;

    const response = await fetch(`${API_BASE_URL}/tasks`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${getToken()}`
        },
        body: JSON.stringify({ task_name: taskName, project_id: projectId })
    });

    if (response.ok) {
        loadTasks();  // Refresh tasks
        document.getElementById("taskForm").reset();
    } else {
        alert("Failed to create task");
    }
}

// ✅ Update Task Status
async function updateTaskStatus(taskId) {
    const response = await fetch(`${API_BASE_URL}/tasks/${taskId}/update`, {
        method: "PUT",
        headers: { "Authorization": `Bearer ${getToken()}` }
    });

    if (response.ok) {
        loadTasks();  // Refresh tasks
    } else {
        alert("Failed to update task");
    }
}

// ✅ Modify loadProjects() to also update the Task Project dropdown
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
        li.innerText = project.project_name;
        projectList.appendChild(li);

        const option = document.createElement("option");
        option.value = project.project_id;
        option.innerText = project.project_name;
        taskProject.appendChild(option);
    });
}

// ✅ Attach event listeners when DOM is loaded
document.addEventListener("DOMContentLoaded", () => {
    if (document.getElementById("taskForm")) {
        document.getElementById("taskForm").addEventListener("submit", createTask);
        loadTasks();
    }
});
