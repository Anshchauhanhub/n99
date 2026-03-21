// public/worker.js

// Make sure to replace this with your actual production backend URL later
const BASE_URL = 'http://localhost:3000/api'; 

function pingActive() {
  fetch(`${BASE_URL}/active-scheduler`)
    .catch((err) => console.error("Active ping failed", err));
}

function pingLazy() {
  fetch(`${BASE_URL}/lazy-scheduler`)
    .catch((err) => console.error("Lazy ping failed", err));
}

// Initial pings
pingActive();
pingLazy();

// Schedulers
setInterval(pingActive, 30000);   // Every 30 seconds
setInterval(pingLazy, 300000);  // Every 5 minutes