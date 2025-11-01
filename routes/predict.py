# routes/predict.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Patient, HealthIndicator, MedicalHistory, Prediction
from schemas.predict import PredictRequest, PredictResponse
from model.pipeline import load_model, prepare_features
import pandas as pd

router = APIRouter(prefix="/predict", tags=["Prediction"])

# Load model once
model = load_model()

@router.post("/", response_model=PredictResponse)
def predict_heart_disease(
    request: PredictRequest,
    db: Session = Depends(get_db)
):
    # 1. Save patient
    patient = Patient(**request.patient.dict())
    db.add(patient)
    db.flush()  # Get patient_id

    # 2. Save health indicators
    hi = HealthIndicator(patient_id=patient.patient_id, **request.health.dict())
    db.add(hi)

    # 3. Save medical history
    mh = MedicalHistory(patient_id=patient.patient_id, **request.medical.dict())
    db.add(mh)

    # 4. Prepare feature vector
    feature_dict = {
        **request.patient.dict(),
        **request.health.dict(),
        **request.medical.dict()
    }
    # Rename to uppercase
    feature_dict = {k.capitalize(): v for k, v in feature_dict.items()}
    feature_dict["HeartDiseaseorAttack"] = 0  # placeholder
    df = pd.DataFrame([feature_dict])
    X = prepare_features(df.drop(columns=["HeartDiseaseorAttack"]))

    # 5. Predict
    prob = model.predict_proba(X)[0][1]
    pred = int(prob >= 0.5)

    # 6. Save prediction
    pred_record = Prediction(
        patient_id=patient.patient_id,
        probability=round(float(prob), 4),
        prediction=pred
    )
    db.add(pred_record)
    db.commit()

    return PredictResponse(
        patient_id=patient.patient_id,
        probability=round(float(prob), 4),
        prediction=pred
    )