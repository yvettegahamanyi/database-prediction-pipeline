from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from formative_1_ml_pipeline.database.postgres_db import SessionLocal
from formative_1_ml_pipeline.crud.pg_crud_health_indicators import (
    create_health_indicator as create_indicator_crud,
    get_health_indicators as get_indicators_crud,
    update_health_indicator as update_indicator_crud,
    delete_health_indicator as delete_indicator_crud,
)
from formative_1_ml_pipeline.schemas.health_indicator_schema import (
    HealthIndicatorBase,
)

router = APIRouter(prefix="/health", tags=["Health Indicators"])

@router.get("/")
def health():
    return {"status": "ok"}