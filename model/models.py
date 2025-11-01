# models.py
from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime, func
from database.postgres_db import Base

class Patient(Base):
    __tablename__ = "patients"
    patient_id = Column(Integer, primary_key=True)
    sex = Column(Float)
    age = Column(Float)
    education = Column(Float)
    income = Column(Float)
    bmi = Column(Float)

class HealthIndicator(Base):
    __tablename__ = "health_indicators"
    indicator_id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"))
    bmi = Column(Float)
    smoker = Column(Integer)
    phys_activity = Column(Integer)
    fruits = Column(Integer)
    veggies = Column(Integer)
    hvy_alcohol_consump = Column(Integer)

class MedicalHistory(Base):
    __tablename__ = "medical_history"
    history_id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"))
    heart_disease_or_attack = Column(Integer)
    high_bp = Column(Integer)
    chol_check = Column(Integer)
    stroke = Column(Integer)
    diabetes = Column(Integer)
    any_healthcare = Column(Integer)
    no_docbc_cost = Column(Integer)
    gen_hlth = Column(Integer)
    ment_hlth = Column(Integer)
    phys_hlth = Column(Integer)
    diff_walk = Column(Integer)

class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"))
    probability = Column(Float)
    prediction = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())