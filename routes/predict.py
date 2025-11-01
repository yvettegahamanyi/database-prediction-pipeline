# routes/predict.py
from fastapi import APIRouter, HTTPException
from schemas.predict import PredictRequest, PredictResponse
from model.pipeline import load_model  # Only load_model
from database import engine
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

            # === 2. INSERT HEALTH INDICATORS ===
            conn.execute(text("""
                INSERT INTO health_indicators 
                (patient_id, bmi, smoker, phys_activity, fruits, veggies, hvy_alcohol_consump)
                VALUES (:pid, :bmi, :smoker, :phys_activity, :fruits, :veggies, :hvy_alcohol_consump)
            """), {
                "pid": patient_id,
                "bmi": request.health.bmi,
                "smoker": request.health.smoker,
                "phys_activity": request.health.phys_activity,
                "fruits": request.health.fruits,
                "veggies": request.health.veggies,
                "hvy_alcohol_consump": request.health.hvy_alcohol_consump
            })

            # === 3. INSERT MEDICAL HISTORY ===
            conn.execute(text("""
                INSERT INTO medical_history 
                (patient_id, high_bp, chol_check, stroke, diabetes,
                 any_healthcare, no_docbc_cost, gen_hlth, ment_hlth, phys_hlth, diff_walk)
                VALUES (:pid, :high_bp, :chol_check, :stroke, :diabetes,
                        :any_healthcare, :no_docbc_cost, :gen_hlth, :ment_hlth, :phys_hlth, :diff_walk)
            """), {
                "pid": patient_id,
                "high_bp": request.medical.high_bp,
                "chol_check": request.medical.chol_check,
                "stroke": request.medical.stroke,
                "diabetes": request.medical.diabetes,
                "any_healthcare": request.medical.any_healthcare,
                "no_docbc_cost": request.medical.no_docbc_cost,
                "gen_hlth": request.medical.gen_hlth,
                "ment_hlth": request.medical.ment_hlth,
                "phys_hlth": request.medical.phys_hlth,
                "diff_walk": request.medical.diff_walk
            })

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

            # Reorder columns to match training
            feature_order = [
                'HighBP','CholCheck','BMI','Smoker','Stroke','Diabetes',
                'PhysActivity','Fruits','Veggies','HvyAlcoholConsump',
                'AnyHealthcare','NoDocbcCost','GenHlth','MentHlth','PhysHlth',
                'DiffWalk','Sex','Age','Education','Income'
            ]
            X = df.reindex(columns=feature_order, fill_value=0)

            # === 6. PREDICT USING FULL PIPELINE (SCALED!) ===
            prob = float(model.predict_proba(X)[0][1])
            pred = int(prob >= 0.5)

            # === 7. SAVE PREDICTION ===
            conn.execute(text("""
                INSERT INTO predictions (patient_id, probability, prediction)
                VALUES (:pid, :prob, :pred)
            """), {"pid": patient_id, "prob": round(prob, 4), "pred": pred})

            # === 8. HUMAN MESSAGE ===
            message = "This person has a heart problem." if pred == 1 else "This person does not have a heart problem."

            return PredictResponse(
                patient_id=patient_id,
                probability=round(prob, 4),
                prediction=pred,
                message=message
            )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")