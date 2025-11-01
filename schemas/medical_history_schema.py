from pydantic import BaseModel, field_validator


class MedicalHistory(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    patient_id: str
    high_bp: float
    high_chol: float
    stroke: float
    heart_disease: float
    diabetes: float

@field_validator(
    "high_bp", "high_chol", "stroke", "heart_disease", "diabetes"
)
def check_positive(cls, value):
    if value < 0:
        raise ValueError("Health indicators must be positive")
    return value



