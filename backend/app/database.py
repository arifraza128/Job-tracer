import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load local environment variables if available (.env in workspace root or backend)
load_dotenv(os.path.join(os.path.dirname(__file__), "../../.env"))
load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://admin:admin@localhost:5432/jobfinder")

print(f"Connecting to database at: {DATABASE_URL}")

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        print("Connected!")
except Exception as e:
    print(f"Database connection failed: {e}")
    print("Ensure that your Docker containers are running (docker compose up -d) and accessible.")
