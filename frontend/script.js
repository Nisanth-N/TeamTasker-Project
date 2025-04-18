document.addEventListener("DOMContentLoaded", function() {
    gsap.from(".logo h1", { opacity: 0, x: -50, duration: 1 });
    gsap.from(".hero h1", { opacity: 0, y: -30, duration: 1 });
    AOS.init();
});

document.addEventListener("DOMContentLoaded", function() {
    console.log("JavaScript Loaded");  // Debugging

    // ✅ Open Login Modal on "Get Started" Click
    document.querySelector("button[onclick='startApp()']").addEventListener("click", function() {
        openModal("login-modal");
    });

    // ✅ Close Modals when clicking 'X'
    document.querySelectorAll(".close-btn").forEach(btn => {
        btn.addEventListener("click", function() {
            closeModal(this.parentElement.parentElement.id);
        });
    });

    // ✅ Ensure modal switching works
    document.querySelectorAll("a[onclick^='switchModal']").forEach(link => {
        link.addEventListener("click", function(event) {
            event.preventDefault();
            const currentModal = this.getAttribute("onclick").match(/'([^']+)'/g)[0].replace(/'/g, "");
            const nextModal = this.getAttribute("onclick").match(/'([^']+)'/g)[1].replace(/'/g, "");
            switchModal(currentModal, nextModal);
        });
    });
});

// ✅ Open Modal
function openModal(modalId) {
    let modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = "flex";
    } else {
        console.error("Modal not found:", modalId);
    }
}

// ✅ Close Modal
function closeModal(modalId) {
    let modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = "none";
    }
}

// ✅ Switch Between Login & Signup
function switchModal(currentModal, nextModal) {
    closeModal(currentModal);
    openModal(nextModal);
}

document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("#login-modal form").addEventListener("submit", function(event) {
        event.preventDefault();  // Prevent page reload

        // Simulate Login Success
        localStorage.setItem("loggedInUser", "John Doe");  // Store user info
        window.location.href = "dashboard.html";  // Redirect to dashboard
    });

    // Display username on Dashboard
    if (window.location.pathname.includes("dashboard.html")) {
        let username = localStorage.getItem("loggedInUser") || "User";
        document.getElementById("username").innerText = username;
    }
});

// ✅ Logout Function
function logout() {
    localStorage.removeItem("loggedInUser");
    window.location.href = "index.html";  // Redirect to homepage
}

function loginUser() {
    let username = document.getElementById("login-username").value;
    let password = document.getElementById("login-password").value;

    if (username === "admin" && password === "password") {
        alert("Login successful!");

        // ✅ Hide the login popup
        document.getElementById("login-popup").style.display = "none";

        // ✅ Show the dashboard section
        document.getElementById("dashboard").style.display = "block";
    } else {
        alert("Invalid credentials. Please try again.");
    }
}
