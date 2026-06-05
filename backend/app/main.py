from fastapi import FastAPI

app = FastAPI(
    title="AI Job Finder API",
    description="API for scraping, embedding, and searching jobs",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "AI Job Finder API"}
