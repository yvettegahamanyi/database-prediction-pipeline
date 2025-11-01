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

router = APIRouter(prefix="/health-indicators", tags=["Health Indicators"]) 


# Dependency for DB session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/{patient_id}")

def create_health_indicator(
    patient_id: int,
    data: HealthIndicatorBase,
    db: Session = Depends(get_db),
):
    """Create a health indicator for a patient."""
    return create_indicator_crud(db, patient_id, data.dict())


@router.get("/{patient_id}")

def get_health_indicators(patient_id: int, db: Session = Depends(get_db)):
    """Get all health indicators for a given patient."""
    return get_indicators_crud(db, patient_id)


@router.put("/{indicator_id}")

def update_health_indicator(
    indicator_id: int,
    data: HealthIndicatorBase,
    db: Session = Depends(get_db),
):
    """Update a specific health indicator."""
    return update_indicator_crud(db, indicator_id, data.dict())


@router.delete("/{indicator_id}")

def delete_health_indicator(indicator_id: int, db: Session = Depends(get_db)):
    """Delete a specific health indicator."""
    return delete_indicator_crud(db, indicator_id)
