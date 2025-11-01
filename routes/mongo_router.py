from fastapi import APIRouter, HTTPException
from crud.mongo_crud import (
    create_patient as create_patient_crud,
    get_patient as get_patient_crud,
    create_health_indicator as create_health_indicator_crud,
    update_health_indicator as update_health_indicator_crud,
)
from schemas.patient_schema import PatientBase
from schemas.health_indicator_schema import HealthIndicatorBase

router = APIRouter(prefix="/mongo", tags=["MongoDB CRUD"])


# Patients
@router.post("/patients")
def create_patient(patient: PatientBase):
    new_id = create_patient_crud(patient.dict(exclude_unset=True))
    return {"_id": new_id}


@router.get("/patients/{patient_id}")
def get_patient(patient_id: str):
    patient = get_patient_crud(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


# Health Indicators
@router.post("/health-indicators")
def create_health_indicator(indicator: HealthIndicatorBase):
    new_id = create_health_indicator_crud(indicator.dict(exclude_unset=True))
    return {"_id": new_id}


@router.put("/health-indicators/{indicator_id}")
def update_health_indicator(indicator_id: str, indicator: HealthIndicatorBase):
    updated = update_health_indicator_crud(
        indicator_id, indicator.dict(exclude_unset=True)
    )
    return updated
