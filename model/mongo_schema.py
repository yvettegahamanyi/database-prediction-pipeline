# app/schemas/mongo_schema.py
from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId


# Helper to convert ObjectId -> string
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class Patient(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    sex: float
    age: float
    education: float
    income: float

    class Config:
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class HealthIndicator(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    patient_id: str
    smoker: float
    phys_activity: float
    fruits: float
    veggies: float
    hvy_alcohol_consump: float

    class Config:
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True
        arbitrary_types_allowed = True