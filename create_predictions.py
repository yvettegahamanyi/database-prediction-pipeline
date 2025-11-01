# create_predictions.py
from database import engine  # Your root database.py
from sqlalchemy import text

print("Creating 'predictions' table...")

with engine.begin() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS predictions (
            id SERIAL PRIMARY KEY,
            patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
            probability FLOAT,
            prediction INTEGER,
            created_at TIMESTAMP DEFAULT NOW()
        )
    """))
    print("predictions table is ready!")