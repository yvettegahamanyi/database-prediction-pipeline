from pydantic import BaseModel, field_validator


class MedicalHistoryBase(BaseModel):
    patient_id: int
    heart_disease_or_attack: float
    high_bp: float
    chol_check: float
    stroke: float
    diabetes: float
    any_healthcare: float
    no_docbc_cost: float
    gen_hlth: float
    ment_hlth: float
    phys_hlth: float
    diff_walk: float

@field_validator(
    "high_bp", "chol_check", "stroke", "heart_disease_or_attack", "diabetes"
)
def check_positive(cls, value):
    if value < 0:
        raise ValueError("Health indicators must be positive")
    return value