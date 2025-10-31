from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
class HealthIndicator(Base):
    __tablename__ = "health_indicators"
    indicator_id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"))
    bmi = Column(Float)
    smoker = Column(Float)
    phys_activity = Column(Float)
    fruits = Column(Float)
    veggies = Column(Float)
    hvy_alcohol_consump = Column(Float)
    patient = relationship("Patient", back_populates="health_indicators")