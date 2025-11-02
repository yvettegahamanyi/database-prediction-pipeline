# models.py
from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime, func
from database.postgres_db import Base

class Patient(Base):
    _tablename_ = "patients"
    patient_id = Column(Integer, primary_key=True)
    sex = Column(Float)
    age = Column(Float)
    education = Column(Float)
    income = Column(Float)

class HealthIndicator(Base):
    _tablename_ = "health_indicators"
    indicator_id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"))
    bmi = Column(Float)
    smoker = Column(Integer)
    phys_activity = Column(Integer)
    fruits = Column(Integer)
    veggies = Column(Integer)
    hvy_alcohol_consump = Column(Integer)

class MedicalHistory(Base):
    _tablename_ = "medical_history"
    history_id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"))
    heart_disease_or_attack = Column(Float, nullable=True)
    high_bp = Column(Float)
    chol_check = Column(Float)
    stroke = Column(Float)
    diabetes = Column(Float)
    any_healthcare = Column(Float)
    no_docbc_cost = Column(Float)
    gen_hlth = Column(Float)
    ment_hlth = Column(Float)
    phys_hlth = Column(Float)
    diff_walk = Column(Float)

class Prediction(Base):
    _tablename_ = "predictions"
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"))
    probability = Column(Float)
    prediction = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())