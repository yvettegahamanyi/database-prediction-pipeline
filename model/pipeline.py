# model/pipeline.py
import os
import joblib
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from dotenv import load_dotenv

load_dotenv()
MODEL_PATH = os.getenv("MODEL_PATH")

FEATURE_ORDER = [
    'HighBP','CholCheck','BMI','Smoker','Stroke','Diabetes',
    'PhysActivity','Fruits','Veggies','HvyAlcoholConsump',
    'AnyHealthcare','NoDocbcCost','GenHlth','MentHlth','PhysHlth',
    'DiffWalk','Sex','Age','Education','Income'
]

def build_pipeline():
    return Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(
            C=0.001, class_weight='balanced', max_iter=1000,
            solver='lbfgs', random_state=42
        ))
    ])

def save_model(model):
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"Model saved: {MODEL_PATH}")

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model not found: {MODEL_PATH}")
    return joblib.load(MODEL_PATH)