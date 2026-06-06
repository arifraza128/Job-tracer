# pyrefly: ignore [missing-import]
from fastapi import FastAPI
from app.routers import auth

app = FastAPI(
    title="AI Job Finder API",
    description="API for scraping, embedding, and searching jobs",
    version="1.0.0"
)

app.include_router(auth.router)

@app.get("/")
def home():
    return {"message": "AI Job Finder API"}
