# AI Job Finder

An AI-powered Job Finder application designed to crawl job opportunities, index them using vector embeddings (via PostgreSQL with pgvector), and present them to users in a premium Next.js dashboard.

## Project Structure

- **`frontend/`**: Next.js (TypeScript, TailwindCSS, App Router) web application dashboard.
- **`backend/`**: FastAPI backend API handling authentication, job indexing, vector search, and user management.
- **`crawler/`**: Job crawler to scrape and ingest job descriptions from various sources.
- **`docker-compose.yml`**: Docker services for local PostgreSQL (with pgvector) and Redis.

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Python 3.10+
- Node.js 18+ (npm or yarn)

### Quick Setup

1. **Start Services (Docker)**:
   ```bash
   docker compose up -d
   ```

2. **Configure Environment Variables**:
   Copy `.env.example` to `.env` and configure your API keys and credentials:
   ```bash
   cp .env.example .env
   ```

3. **Backend Setup**:
   ```bash
   cd backend
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/macOS:
   source venv/bin/activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```

4. **Frontend Setup**:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
