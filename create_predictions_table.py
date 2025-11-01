# create_predictions_table.py
from database import engine
from models import Prediction
from sqlalchemy import text

with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS predictions (
            id SERIAL PRIMARY KEY,
            patient_id INTEGER REFERENCES patients(patient_id),
            probability FLOAT,
            prediction INTEGER,
            created_at TIMESTAMP DEFAULT NOW()
        )
    """))
    conn.commit()
print("predictions table ready")