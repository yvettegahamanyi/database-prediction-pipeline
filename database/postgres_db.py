# crud/db/connection.py
import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
    f"@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
)

# Use psycopg (psycopg3) for Python 3.13 compatibility
# Replace postgresql:// with postgresql+psycopg:// to use psycopg3 driver
if DATABASE_URL.startswith("postgresql://"):
    try:
        # Try to import psycopg to see if it's available
        import psycopg
        DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg://", 1)
    except ImportError:
        # Fall back to psycopg2 if psycopg is not available
        # This will work for Python < 3.13
        pass

engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

def test_connection():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print("DB Connected!")
            return True
    except Exception as e:
        print(f"Connection failed: {e}")
        return False

if __name__ == "__main__":
    test_connection()