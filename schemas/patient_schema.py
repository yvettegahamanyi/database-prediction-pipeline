from pydantic import BaseModel, validator

class PatientBase(BaseModel):
    sex: float
    age: float
    education: float
    income: float

    @validator("sex", "age", "education", "income")
    def validate_float(cls, v):
        """Ensure value is a float"""
        if not isinstance(v, float):
            raise ValueError("Value must be a float")
        return v