# schemas/predict.py
from pydantic import BaseModel
from typing import Optional

class PatientInput(BaseModel):
    sex: int
    age: int
    education: Optional[int] = None
    income: Optional[int] = None

class HealthIndicatorInput(BaseModel):
    bmi: float
    smoker: int
    phys_activity: int
    fruits: int
    veggies: int
    hvy_alcohol_consump: int

class MedicalHistoryInput(BaseModel):
    high_bp: int
    chol_check: int
    stroke: int
    diabetes: int
    any_healthcare: int
    no_docbc_cost: int
    gen_hlth: int
    ment_hlth: int
    phys_hlth: int
    diff_walk: int

class PredictRequest(BaseModel):
    patient: PatientInput
    health: HealthIndicatorInput
    medical: MedicalHistoryInput

class PredictResponse(BaseModel):
    patient_id: int
    probability: float
    prediction: int
    message: str = "Prediction saved"