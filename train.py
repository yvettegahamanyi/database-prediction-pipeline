# train.py
import pandas as pd
from sqlalchemy import text
from database.postgres_db import engine
from model.pipeline import build_pipeline, save_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    roc_auc_score, accuracy_score, precision_score,
    recall_score, f1_score
)
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline

print("Starting training with SMOTE augmentation...")

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
    'high_bp': 'HighBP', 'chol_check': 'CholCheck', 'phys_activity': 'PhysActivity',
    'hvy_alcohol_consump': 'HvyAlcoholConsump', 'any_healthcare': 'AnyHealthcare',
    'no_docbc_cost': 'NoDocbcCost', 'gen_hlth': 'GenHlth', 'ment_hlth': 'MentHlth',
    'phys_hlth': 'PhysHlth', 'diff_walk': 'DiffWalk', 'bmi': 'BMI',
    'smoker': 'Smoker', 'stroke': 'Stroke', 'diabetes': 'Diabetes',
    'fruits': 'Fruits', 'veggies': 'Veggies', 'sex': 'Sex',
    'age': 'Age', 'education': 'Education', 'income': 'Income'
})

# === 3. CLEAN DATA ===
df = df.dropna(subset=['HeartDiseaseorAttack'])
print(f"After cleaning: {len(df)} samples")

# === 4. PREPARE X AND y ===
X = df.drop(columns=['HeartDiseaseorAttack'], errors='ignore')
y = df['HeartDiseaseorAttack']

# === 5. TRAIN/TEST SPLIT (BEFORE AUGMENTATION!) ===
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)
print(f"Training set: {len(X_train)} | Test set: {len(X_test)}")

# === 6. BUILD PIPELINE WITH SMOTE ===
pipeline = ImbPipeline([
    ('imputer', 'passthrough'),  # SMOTE handles NaN
    ('smote', SMOTE(random_state=42)),
    ('scaler', 'passthrough'),
    ('classifier', 'passthrough')
])

# We'll fit step-by-step to control augmentation
print("Applying SMOTE to training data...")
X_train_aug, y_train_aug = SMOTE(random_state=42).fit_resample(X_train, y_train)
print(f"After SMOTE: {len(X_train_aug)} samples (balanced)")

# === 7. TRAIN FINAL MODEL ON AUGMENTED DATA ===
final_pipeline = build_pipeline()  # imputer + scaler + logreg
final_pipeline.fit(X_train_aug, y_train_aug)

# === 8. EVALUATE ON ORIGINAL TEST SET ===
y_prob = final_pipeline.predict_proba(X_test)[:, 1]
y_pred = final_pipeline.predict(X_test)

auc = roc_auc_score(y_test, y_prob)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\n" + "="*60)
print("MODEL EVALUATION (WITH SMOTE AUGMENTATION)")
print("="*60)
print(f"AUC-ROC       : {auc:.4f}")
print(f"Accuracy      : {accuracy:.4f}")
print(f"Precision     : {precision:.4f}")
print(f"Recall        : {recall:.4f} ")
print(f"F1-Score      : {f1:.4f}")
print("="*60)

# === 9. RETRAIN ON FULL ORIGINAL DATA (Production) ===
print("Retraining on full original data for deployment...")
final_pipeline.fit(X, y)

# === 10. SAVE MODEL ===
save_model(final_pipeline)
print("Final model saved: model/logreg_model.joblib")
print("Training + SMOTE + Evaluation complete!")