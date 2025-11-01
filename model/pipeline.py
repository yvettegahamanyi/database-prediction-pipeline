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
# MODEL_PATH = os.getenv("MODEL_PATH")

# Get the directory where this file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Get MODEL_PATH from env, or use default relative to this file
_model_path = os.getenv("MODEL_PATH", "logreg_model.joblib")
if os.path.isabs(_model_path):
    MODEL_PATH = _model_path
elif _model_path.startswith("model/"):
    # If path starts with "model/", use it relative to project root
    # Go up one directory from BASE_DIR (model/) to get project root
    PROJECT_ROOT = os.path.dirname(BASE_DIR)
    MODEL_PATH = os.path.join(PROJECT_ROOT, _model_path)
else:
    # If relative path, resolve it relative to this file's directory
    MODEL_PATH = os.path.join(BASE_DIR, _model_path)

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
        raise FileNotFoundError(f"Model not found: {MODEL_PATH}. Train first.")
    return joblib.load(MODEL_PATH)

# THIS IS THE FUNCTION WE NEED
def prepare_features(df: pd.DataFrame) -> pd.DataFrame:
    """Reorder and return only the 20 features in correct order."""
    return df[FEATURE_ORDER].copy()