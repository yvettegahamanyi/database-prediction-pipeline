# routes/pg_health_indicators.py
from fastapi import APIRouter
from database.postgres_db import engine  # Only engine
from sqlalchemy import text

router = APIRouter(prefix="/health", tags=["Health Indicators"])

@router.get("/")
def health_check():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"status": "ok", "database": "connected"}
    except Exception as e:
        return {"status": "error", "database": "disconnected", "detail": str(e)}