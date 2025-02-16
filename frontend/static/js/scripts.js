const API_BASE_URL = "/api";  // Ensure Flask API is correctly proxied by NGINX

// ✅ Check if user is authenticated
function checkAuth() {
    const token = getToken();
    if (!token) {
        window.location.href = "/login.html";  // Redirect to login page if not authenticated
    }
}

// ✅ Get JWT token from local storage
function getToken() {
    return localStorage.getItem("token");
}

// ✅ Logout function
function logout() {
    localStorage.removeItem("token");
    window.location.href = "/login.html";
}

// ✅ Fetch and display user's projects
async function fetchUserProjects() {
    checkAuth();
    const headers = { "Authorization": `Bearer ${getToken()}` };

    try {
        const response = await fetch(`${API_BASE_URL}/user/projects`, { headers });
        const projects = await response.json();

        const projectList = document.getElementById("userProjects");
        projectList.innerHTML = "";

        projects.forEach(project => {
            const li = document.createElement("li");
            li.textContent = project.name;
            li.classList.add("list-group-item");
            projectList.appendChild(li);
        });
    } catch (error) {
        console.error("Error fetching projects:", error);
    }
}

// ✅ Fetch and display user's tasks
async function fetchUserTasks() {
    checkAuth();
    const headers = { "Authorization": `Bearer ${getToken()}` };

    try {
        const response = await fetch(`${API_BASE_URL}/user/tasks`, { headers });
        const tasks = await response.json();

        const taskList = document.getElementById("userTasks");
        taskList.innerHTML = "";

        tasks.forEach(task => {
            const li = document.createElement("li");
            li.textContent = `${task.title} - ${task.status}`;
            li.classList.add("list-group-item");
            taskList.appendChild(li);
        });
    } catch (error) {
        console.error("Error fetching tasks:", error);
    }
}

// ✅ Login function
async function loginUser(event) {
    event.preventDefault();
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try {
        const response = await fetch(`${API_BASE_URL}/login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();

        if (response.ok) {
            localStorage.setItem("token", data.access_token);
            window.location.href = "/";
        } else {
            document.getElementById("errorMessage").textContent = "Invalid login credentials.";
        }
    } catch (error) {
        console.error("Error logging in:", error);
    }
}

// ✅ Create a new project
async function createProject(event) {
    event.preventDefault();
    checkAuth();
    const projectName = document.getElementById("projectName").value;
    const headers = { 
        "Authorization": `Bearer ${getToken()}`,
        "Content-Type": "application/json"
    };

    try {
        const response = await fetch(`${API_BASE_URL}/projects`, {
            method: "POST",
            headers,
            body: JSON.stringify({ name: projectName })
        });

        if (response.ok) {
            fetchUserProjects();  // Refresh project list
            document.getElementById("projectName").value = "";  // Clear input field
        } else {
            console.error("Failed to create project.");
        }
    } catch (error) {
        console.error("Error creating project:", error);
    }
}

// ✅ Create a new task
async function createTask(event) {
    event.preventDefault();
    checkAuth();
    const taskName = document.getElementById("taskName").value;
    const taskProjectId = document.getElementById("taskProject").value;
    const headers = { 
        "Authorization": `Bearer ${getToken()}`,
        "Content-Type": "application/json"
    };

    try {
        const response = await fetch(`${API_BASE_URL}/tasks`, {
            method: "POST",
            headers,
            body: JSON.stringify({ title: taskName, project_id: taskProjectId })
        });

        if (response.ok) {
            fetchUserTasks();  // Refresh task list
            document.getElementById("taskName").value = "";  // Clear input field
        } else {
            console.error("Failed to create task.");
        }
    } catch (error) {
        console.error("Error creating task:", error);
    }
}

// ✅ Load user data when the page is ready
document.addEventListener("DOMContentLoaded", () => {
    if (window.location.pathname === "/") {
        fetchUserProjects();
        fetchUserTasks();
    }

    // Attach event listeners
    const loginForm = document.getElementById("loginForm");
    if (loginForm) loginForm.addEventListener("submit", loginUser);

    const projectForm = document.getElementById("projectForm");
    if (projectForm) projectForm.addEventListener("submit", createProject);

    const taskForm = document.getElementById("taskForm");
    if (taskForm) taskForm.addEventListener("submit", createTask);
});
