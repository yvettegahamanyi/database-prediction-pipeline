# schemas/health_indicator_schema.py
from pydantic import BaseModel, validator


class HealthIndicatorBase(BaseModel):
    smoker: float
    phys_activity: float
    fruits: float
    veggies: float
    hvy_alcohol_consump: float

    @validator("smoker", "phys_activity", "fruits", "veggies", "hvy_alcohol_consump")
    def validate_booleanish(cls, v):
        """Ensure value is either 0 or 1 (int or float)"""
        if v not in [0, 1, 0.0, 1.0]:
            raise ValueError("Value must be 0, 1, 0.0, or 1.0")
        return float(v)
