from fastapi import APIRouter, HTTPException
from crud.mongo_crud import (
    create_patient as create_patient_crud,
    get_patient as get_patient_crud,
    create_health_indicator as create_health_indicator_crud,
    update_health_indicator as update_health_indicator_crud,
    create_medical_history as create_medical_history_crud,
    get_medical_history as get_medical_history_crud,
    get_all_medical_histories as get_all_medical_histories_crud,
    update_medical_history as update_medical_history_crud,
    delete_medical_history as delete_medical_history_crud,
)
from schemas.patient_schema import PatientBase
from schemas.health_indicator_schema import HealthIndicatorBase
from schemas.medical_history_schema import MedicalHistoryBase

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


# medical history routes

@router.post("/medical-history")
def create_medical_history(history: MedicalHistoryBase):
    new_id = create_medical_history_crud(history)
    return {"_id": new_id}      

@router.get("/medical-history/{history_id}")
def get_medical_history(history_id: str):
    history = get_medical_history_crud(history_id)
    if not history:
        raise HTTPException(status_code=404, detail="Medical history not found")
    return history

@router.get("/medical-history")
def get_all_medical_histories():
    histories = get_all_medical_histories_crud()
    return histories

@router.put("/medical-history/{history_id}")
def update_medical_history(history_id: str, history: MedicalHistoryBase): 
    updated = update_medical_history_crud(
        history_id, history
    )
    return updated  


@router.delete("/medical-history/{history_id}")
def delete_medical_history(history_id: str):            
    success = delete_medical_history_crud(history_id)
    if not success:
        raise HTTPException(status_code=404, detail="Medical history not found")
    return {"message": "Medical history deleted successfully"}