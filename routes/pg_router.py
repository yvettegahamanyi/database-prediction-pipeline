from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.postgres_db import get_db
from crud.pg_crud import (
    create_patient as create_patient_crud,
    get_patient as get_patient_crud,
    update_patient as update_patient_crud,
    create_health_indicator as create_indicator_crud,
    get_health_indicators as get_indicators_crud,
    update_health_indicator as update_indicator_crud,
    delete_health_indicator as delete_indicator_crud,
    create_medical_history as create_medical_history_crud,
    get_medical_history as get_medical_history_crud,
    get_all_medical_histories as get_all_medical_histories_crud,
    update_medical_history as update_medical_history_crud,
    delete_medical_history as delete_medical_history_crud,
)
from schemas.health_indicator_schema import (
    HealthIndicatorBase,
)
from schemas.patient_schema import PatientBase
from schemas.medical_history_schema import MedicalHistoryBase

router = APIRouter(prefix="/pg", tags=["PostgreSQL CRUD"])


# Dependency for DB session

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


@router.post("/patients")
async def create_patient(patient: PatientBase, db: Session = Depends(get_db)):
    return create_patient_crud(db, patient.dict())


@router.get("/patients/{patient_id}")
async def get_patient(patient_id: int, db: Session = Depends(get_db)):
    return get_patient_crud(db, patient_id)


@router.put("/patients/{patient_id}")
async def update_patient(
    patient_id: int, patient: PatientBase, db: Session = Depends(get_db)
):
    return update_patient_crud(db, patient_id, patient.dict())


@router.post("/health-indicators/{patient_id}")
async def create_health_indicator(
    patient_id: int,
    data: HealthIndicatorBase,
    db: Session = Depends(get_db),
):
    """Create a health indicator for a patient."""
    return create_indicator_crud(db, patient_id, data.dict())


@router.get("/health-indicators/{patient_id}")
async def get_health_indicators(patient_id: int, db: Session = Depends(get_db)):
    """Get all health indicators for a given patient."""
    return get_indicators_crud(db, patient_id)


@router.put("/health-indicators/{indicator_id}")
async def update_health_indicator(
    indicator_id: int,
    data: HealthIndicatorBase,
    db: Session = Depends(get_db),
):
    """Update a specific health indicator."""
    return update_indicator_crud(db, indicator_id, data.dict())


@router.delete("/health-indicators/{indicator_id}")
async def delete_health_indicator(
    indicator_id: int, db: Session = Depends(get_db)
):
    """Delete a specific health indicator."""
    return delete_indicator_crud(db, indicator_id)

# medical history endpoints

@router.post("/medical-history")
async def create_medical_history(   
    patient_id: int,
    data: MedicalHistoryBase,
    db: Session = Depends(get_db),
):
    """Create a medical history for a patient."""
    return create_medical_history_crud(db, patient_id, data)

@router.get("/medical-history/{patient_id}")
async def get_medical_history(patient_id: int, db: Session = Depends(get_db)):  
    """Get medical history for a given patient."""
    return get_medical_history_crud(db, patient_id) 

@router.put("/medical-history/{history_id}")
async def update_medical_history(
    history_id: int,
    data: dict,
    db: Session = Depends(get_db),
):
    """Update a specific medical history record."""
    return update_medical_history_crud(db, history_id, data)    


@router.delete("/medical-history/{history_id}")
async def delete_medical_history(
    history_id: int, db: Session = Depends(get_db)
):
    """Delete a specific medical history record."""
    return delete_medical_history_crud(db, history_id)