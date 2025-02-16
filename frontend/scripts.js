// API Base URL (Now uses the same origin to avoid CORS issues)
const API_BASE_URL = "/api"; // ✅ Requests go through NGINX

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
