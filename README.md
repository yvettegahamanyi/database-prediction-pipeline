
# Heart Disease Prediction Pipeline

A full-stack database and machine learning pipeline for heart disease prediction, featuring PostgreSQL and MongoDB databases, FastAPI REST endpoints, and automated prediction workflows.

##  Dataset

[Heart Disease Health Indicators Dataset](https://www.kaggle.com/datasets/alexteboul/heart-disease-health-indicators-dataset/data) from Kaggle

## Team Members

- Yvette Gahamanyi
- Pretty Diane Ntakirutimana
- Elyse Marie Uyiringiye
- Best Verie Iradukunda

## Architecture

### Database Schema (PostgreSQL)

- **patients**: Demographics (sex, age, education, income)
- **health_indicators**: Lifestyle factors (BMI, smoking, physical activity, diet, alcohol)
- **medical_history**: Health conditions (heart disease, blood pressure, cholesterol, diabetes, stroke)
- **predictions**: ML model prediction results

### NoSQL (MongoDB)

Mirrored collections with embedded document structure for flexible querying.

##  Features

### Database
- ✅ Normalized schema (3NF)
- ✅ Stored procedure: `add_patient_record()`
- ✅ Trigger: `validate_healthcare_access()`
- ✅ Foreign key constraints with CASCADE delete
- ✅ ERD diagram (DBML format)

### API (FastAPI)
- ✅ Full CRUD operations for all tables
- ✅ Input validation with Pydantic
- ✅ Error handling
- ✅ Supports both PostgreSQL and MongoDB

### ML Pipeline
-  Fetch latest patient data via API
-  Data preprocessing and validation
-  Heart disease prediction
-  Store results back to database

## Installation

1. Clone the repository
```bash
git clone https://github.com/yvettegahamanyi/database-prediction-pipeline.git
cd database-prediction-pipeline
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Set up your databases (PostgreSQL and MongoDB)

4. Run the application

##  Running Predictions

Run the prediction script to fetch latest patient data and make predictions:

```bash
python predict.py
```

##  Database Features

**Stored Procedure:** `add_patient_record()` - Adds patient data across multiple tables in one transaction

**Trigger:** `validate_healthcare_access()` - Validates data integrity for healthcare-related fields

##  Technologies Used

- **Backend:** FastAPI
- **Databases:** PostgreSQL, MongoDB
- **ML:** Scikit-learn
- **Python Libraries:** Pandas, NumPy


## Contributing

This is an academic project.

## Contact

For inquiries, please contact any team member through the repository.