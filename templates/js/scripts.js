const API_BASE_URL = "/api";

async function fetchUserData() {
    checkAuth();
    const headers = { "Authorization": `Bearer ${getToken()}` };

    try {
        // Fetch projects
        const projectRes = await fetch(`${API_BASE_URL}/user/projects`, { headers });
        const projects = await projectRes.json();
        displayUserProjects(projects);

        // Fetch tasks
        const taskRes = await fetch(`${API_BASE_URL}/user/tasks`, { headers });
        const tasks = await taskRes.json();
        displayUserTasks(tasks);
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

// Display user projects
function displayUserProjects(projects) {
    const projectList = document.getElementById("userProjects");
    projectList.innerHTML = "";
    projects.forEach(project => {
        const li = document.createElement("li");
        li.textContent = project.name;
        li.classList.add("list-group-item");
        projectList.appendChild(li);
    });
}

// Display user tasks
function displayUserTasks(tasks) {
    const taskList = document.getElementById("userTasks");
    taskList.innerHTML = "";
    tasks.forEach(task => {
        const li = document.createElement("li");
        li.textContent = `${task.title} - ${task.status}`;
        li.classList.add("list-group-item");
        taskList.appendChild(li);
    });
}

// Fetch user data on page load
document.addEventListener("DOMContentLoaded", fetchUserData);
