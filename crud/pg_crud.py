from sqlalchemy.orm import Session
from fastapi import HTTPException
from model.models import Patient, HealthIndicator

# add apis for patients
def create_patient(db: Session, data: dict):
    """Create a patient record."""
    patient = Patient(**data)
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient
    
def get_patient(db: Session, patient_id: int):
    """Get a patient record."""
    return db.query(Patient).filter(Patient.patient_id == patient_id).first()
    
def update_patient(db: Session, patient_id: int, data: dict):
    """Update a patient record."""
    patient = db.query(Patient).filter(Patient.patient_id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail=f"Patient with ID {patient_id} not found")
    for key, value in data.items():
        if hasattr(patient, key):
            setattr(patient, key, value)
    db.commit()
    db.refresh(patient)
    return patient


def create_health_indicator(db: Session, patient_id: int, data: dict):
    """Create a health indicator for a given patient."""
    # Check if patient exists
    patient = db.query(Patient).filter(Patient.patient_id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail=f"Patient with ID {patient_id} not found")

    health_indicator = HealthIndicator(
        patient_id=patient_id,
        bmi=data.get("bmi"),
        smoker=data.get("smoker"),
        phys_activity=data.get("phys_activity"),
        fruits=data.get("fruits"),
        veggies=data.get("veggies"),
        hvy_alcohol_consump=data.get("hvy_alcohol_consump")
    )

    db.add(health_indicator)
    db.commit()
    db.refresh(health_indicator)
    return health_indicator


def get_health_indicators(db: Session, patient_id: int):
    """Retrieve all health indicators for a given patient."""
    indicators = db.query(HealthIndicator).filter(HealthIndicator.patient_id == patient_id).all()
    if not indicators:
        raise HTTPException(status_code=404, detail=f"No health indicators found for patient ID {patient_id}")
    return indicators


def update_health_indicator(db: Session, indicator_id: int, data: dict):
    """Update a health indicator record."""
    indicator = db.query(HealthIndicator).filter(HealthIndicator.indicator_id == indicator_id).first()
    if not indicator:
        raise HTTPException(status_code=404, detail=f"Health indicator with ID {indicator_id} not found")

    for key, value in data.items():
        if hasattr(indicator, key):
            setattr(indicator, key, value)

    db.commit()
    db.refresh(indicator)
    return indicator


def delete_health_indicator(db: Session, indicator_id: int):
    """Delete a health indicator record."""
    indicator = db.query(HealthIndicator).filter(HealthIndicator.indicator_id == indicator_id).first()
    if not indicator:
        raise HTTPException(status_code=404, detail=f"Health indicator with ID {indicator_id} not found")

    db.delete(indicator)
    db.commit()
    return {"message": f"Health indicator ID {indicator_id} deleted successfully"}


#  Medical History CRUD operations
def create_medical_history(db: Session, patient_id: int, data: dict):  
    """Create a medical history for a given patient."""
    # Check if patient exists
    patient = db.query(Patient).filter(Patient.patient_id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail=f"Patient with ID {patient_id} not found")

    medical_history = MedicalHistory(
        patient_id=patient_id,
        high_bp=data.get("high_bp"),
        high_chol=data.get("high_chol"),
        stroke=data.get("stroke"),
        heart_disease=data.get("heart_disease"),
        diabetes=data.get("diabetes")
    )

    db.add(medical_history)
    db.commit()
    db.refresh(medical_history)
    return medical_history

