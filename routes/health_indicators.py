# routes/health_indicators.py
from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health Indicators"])

@router.get("/")
def health():
    return {"status": "ok"}