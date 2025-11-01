# create_predictions.py
from crud.db.connection import engine
from sqlalchemy import text

with engine.begin() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS predictions (
            id SERIAL PRIMARY KEY,
            patient_id INTEGER REFERENCES patients(patient_id),
            probability FLOAT,
            prediction INTEGER,
            created_at TIMESTAMP DEFAULT NOW()
        )
    """))
print("predictions table ready")