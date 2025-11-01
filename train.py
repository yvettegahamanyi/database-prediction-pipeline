# train.py
import pandas as pd
from sqlalchemy import text
from database.postgres_db import engine
from model.pipeline import build_pipeline, save_model, prepare_features

print("Starting training...")

# === 1. PULL DATA FROM DB ===
query = """
SELECT 
    p.sex, p.age, p.education, p.income,
    hi.bmi, hi.smoker, hi.phys_activity, hi.fruits, hi.veggies, hi.hvy_alcohol_consump,
    mh.heart_disease_or_attack,
    mh.high_bp, mh.chol_check, mh.stroke, mh.diabetes,
    mh.any_healthcare, mh.no_docbc_cost, mh.gen_hlth,
    mh.ment_hlth, mh.phys_hlth, mh.diff_walk
FROM patients p
JOIN health_indicators hi ON p.patient_id = hi.patient_id
JOIN medical_history mh ON p.patient_id = mh.patient_id
"""

print("Fetching data from database...")
df = pd.read_sql(query, engine)

if df.empty:
    print("No data found! Add rows to the tables first.")
    exit()

print(f"Loaded {len(df)} samples")

# === 2. RENAME COLUMNS ===
df = df.rename(columns={
    'heart_disease_or_attack': 'HeartDiseaseorAttack',
    'high_bp': 'HighBP',
    'chol_check': 'CholCheck',
    'phys_activity': 'PhysActivity',
    'hvy_alcohol_consump': 'HvyAlcoholConsump',
    'any_healthcare': 'AnyHealthcare',
    'no_docbc_cost': 'NoDocbcCost',
    'gen_hlth': 'GenHlth',
    'ment_hlth': 'MentHlth',
    'phys_hlth': 'PhysHlth',
    'diff_walk': 'DiffWalk',
    'bmi': 'BMI',
    'smoker': 'Smoker',
    'stroke': 'Stroke',
    'diabetes': 'Diabetes',
    'fruits': 'Fruits',
    'veggies': 'Veggies',
    'sex': 'Sex',
    'age': 'Age',
    'education': 'Education',
    'income': 'Income'
})

print("Columns after rename:", df.columns.tolist())

# === 3. CLEAN DATA: Remove rows where target is NaN ===
print(f"Before cleaning: {len(df)} samples")
df = df.dropna(subset=['HeartDiseaseorAttack'])
print(f"After cleaning: {len(df)} samples")

# === 4. PREPARE X AND y ===
X = prepare_features(df.drop(columns=['HeartDiseaseorAttack'], errors='ignore'))
y = df['HeartDiseaseorAttack']

print(f"Training on {X.shape[1]} features")
print(f"Class balance:\n{y.value_counts(normalize=True)}")

# === 5. TRAIN MODEL ===
pipeline = build_pipeline()
pipeline.fit(X, y)

# === 6. SAVE MODEL ===
save_model(pipeline)
print("Training complete! Model saved at model/logreg_model.joblib")