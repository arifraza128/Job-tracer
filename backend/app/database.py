import os
# pyrefly: ignore [missing-import]
from sqlalchemy import create_engine
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import sessionmaker, declarative_base
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

# Load local environment variables if available (.env in workspace root or backend)
load_dotenv(os.path.join(os.path.dirname(__file__), "../../.env"))
load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://admin:admin@localhost:5432/jobfinder")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    print(f"Testing connection to database at: {DATABASE_URL}")
    try:
        with engine.connect() as conn:
            print("Successfully connected to the database!")
    except Exception as e:
        print(f"Database connection failed: {e}")
