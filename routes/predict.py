# routes/predict.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.postgres_db import get_db
from model.models import Patient, HealthIndicator, MedicalHistory, Prediction
from schemas.predict import PredictRequest, PredictResponse
from model.pipeline import load_model  # Only load_model
from database.postgres_db import engine
from sqlalchemy import text
import pandas as pd

router = APIRouter(prefix="/predict", tags=["Prediction"])

# Load trained pipeline (imputer + scaler + model)
model = load_model()


@router.post("/", response_model=PredictResponse)
def predict_heart_disease(request: PredictRequest):
    try:
        with engine.begin() as conn:
            # === 1. INSERT PATIENT ===
            result = conn.execute(text("""
                INSERT INTO patients (sex, age, education, income)
                VALUES (:sex, :age, :education, :income)
                RETURNING patient_id
            """), {
                "sex": request.patient.sex,
                "age": request.patient.age,
                "education": request.patient.education or 0,
                "income": request.patient.income or 0
            })
            patient_id = result.scalar()

    # 2. Save health indicators
    hi = HealthIndicator(
        patient_id=patient.patient_id, **request.health.dict()
    )
    db.add(hi)

    # 3. Save medical history
    mh = MedicalHistory(
        patient_id=patient.patient_id, **request.medical.dict()
    )
    db.add(mh)

            # === 4. BUILD FEATURE DICT ===
            feature_dict = {
                **request.patient.dict(),
                **request.health.dict(),
                **request.medical.dict()
            }

            # Map input keys to model column names
            rename_map = {
                'high_bp': 'HighBP', 'chol_check': 'CholCheck', 'bmi': 'BMI',
                'smoker': 'Smoker', 'stroke': 'Stroke', 'diabetes': 'Diabetes',
                'phys_activity': 'PhysActivity', 'fruits': 'Fruits', 'veggies': 'Veggies',
                'hvy_alcohol_consump': 'HvyAlcoholConsump', 'any_healthcare': 'AnyHealthcare',
                'no_docbc_cost': 'NoDocbcCost', 'gen_hlth': 'GenHlth', 'ment_hlth': 'MentHlth',
                'phys_hlth': 'PhysHlth', 'diff_walk': 'DiffWalk',
                'sex': 'Sex', 'age': 'Age', 'education': 'Education', 'income': 'Income'
            }
            feature_dict = {rename_map.get(k, k): v for k, v in feature_dict.items()}

            # === 5. CREATE DATAFRAME WITH EXACT ORDER ===
            df = pd.DataFrame([feature_dict])

    return PredictResponse(
        patient_id=patient.patient_id,
        probability=round(float(prob), 4),
        prediction=pred
    )
