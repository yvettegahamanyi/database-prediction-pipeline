# train.py
import pandas as pd
from sqlalchemy import text
from database import engine
from model.pipeline import build_pipeline, save_model, prepare_features

print("Starting training...")

# Step 1: Pull and join data
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
    print("No data found!")
    exit()

print(f"Loaded {len(df)} samples")

# Step 2: Rename to match model (uppercase)
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

# Step 3: Prepare features
X = prepare_features(df.drop(columns=['HeartDiseaseorAttack']))
y = df['HeartDiseaseorAttack']

print(f"Training on {X.shape[1]} features")
print(f"Class balance:\n{y.value_counts(normalize=True)}")

# Step 4: Train
pipeline = build_pipeline()
pipeline.fit(X, y)

# Step 5: Save
save_model(pipeline)
print("Training complete! Model ready at model/logreg_model.joblib")