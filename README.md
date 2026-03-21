<div align="center">

<img src="client/src/assets/n99_logo.png" alt="n99 Logo" width="240" onerror="this.style.display='none'">

**Intelligent Movie Ticket Availability Tracker**

[![Vue 3](https://img.shields.io/badge/Vue%203-4FC08D?style=flat-square&logo=vue.js&logoColor=white)](https://vuejs.org/)
[![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white)](https://vitejs.dev/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python 3](https://img.shields.io/badge/Python%203-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)

</div>

## What is n99?

n99 is an automated movie ticket tracking application that monitors cinema websites for ticket availability and notifies users the moment tickets go on sale. Never miss opening night again.

## Features

| Feature | Description |
|---------|-------------|
| **Smart Tracking** | Select movie, cinema, and date to track availability |
| **Real-time Notifications** | Instant email alerts when tickets become available |
| **Background Automation** | Automated scraping with Playwright & Selenium |
| **Job Scheduling** | APScheduler handles periodic checks efficiently |
| **User Profiles** | Persistent user preferences and tracking history |

## Tech Stack

### Frontend
- **Vue 3** - Progressive JavaScript framework
- **Vite** - Next-generation frontend tooling
- **Modern CSS** - Clean, responsive UI

### Backend
- **FastAPI** - High-performance Python web framework
- **Uvicorn** - Lightning-fast ASGI server
- **PostgreSQL** - Robust relational database (via psycopg)
- **Redis** - In-memory data structure store for caching & sessions
- **APScheduler** - Advanced Python Scheduler for background tasks
- **Playwright & Selenium** - Browser automation for web scraping
- **SendInBlue (Brevo)** - Email delivery service

## Project Structure

```
n99/
├── client/              # Vue.js frontend
│   ├── src/
│   │   ├── assets/      # Static assets
│   │   ├── main.js      # Application entry
│   │   └── style.css    # Global styles
│   ├── index.html       # Main HTML template
│   └── package.json     # Frontend dependencies
│
└── server/              # FastAPI backend
    ├── src/
    │   ├── config/      # Application configuration
    │   ├── model/       # Database models
    │   ├── router/      # API routes
    │   ├── services/    # Business logic
    │   │   ├── mail/    # Email templates & service
    │   │   └── scheduler/  # Background job schedulers
    │   └── assets/      # Server assets
    ├── main.py          # Application entry point
    └── requirements.txt # Python dependencies
```

## Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- PostgreSQL
- Redis

### Backend Setup

```bash
cd server
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your database and API credentials

# Start the server
python main.py
```

Server runs at `http://localhost:8000`

### Frontend Setup

```bash
cd client
npm install
npm run dev
```

Client runs at `http://localhost:5173`

## Environment Variables

Create a `.env` file in the `server/` directory:

```env
# Database
DATABASE_URL=postgresql://user:password@localhost/n99

# Redis
REDIS_URL=redis://localhost:6379/0

# Email (SendInBlue/Brevo)
SENDINBLUE_API_KEY=your_api_key_here

# Application
SECRET_KEY=your-secret-key-here
DEBUG=false
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/users` | Create/update user profile |
| `GET` | `/users/{user_id}` | Get user details |
| `POST` | `/tracking` | Start tracking a movie |
| `GET` | `/tracking/{tracking_id}` | Get tracking status |
| `DELETE` | `/tracking/{tracking_id}` | Stop tracking |

## Deployment

The application is designed to run as separate services:

```bash
# Production server
uvicorn server.main:app --host 0.0.0.0 --port 8000 --workers 4

# Production client build
npm run build  # Outputs to dist/
```

Consider using Docker Compose for orchestration:
- Web server (FastAPI)
- Frontend (Nginx)
- PostgreSQL
- Redis
- Worker processes for schedulers

## Contributing

Contributions are welcome! Please follow the existing code style and add tests for new features.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under GNU v3.0. See the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Never miss a movie again with n99**

</div>