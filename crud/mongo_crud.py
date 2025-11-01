from database.mongo_db import (
    patients_collection,
    health_indicators_collection,
)
from bson import ObjectId


# 🧍 Patients CRUD
def create_patient(patient: dict):
    result = patients_collection.insert_one(patient)
    return str(result.inserted_id)


def get_patient(patient_id: str):
    return patients_collection.find_one({"_id": ObjectId(patient_id)})


def get_all_patients():
    return list(patients_collection.find())


def update_patient(patient_id: str, update_data: dict):
    patients_collection.update_one(
        {"_id": ObjectId(patient_id)}, {"$set": update_data}
    )
    return get_patient(patient_id)


def delete_patient(patient_id: str):
    patients_collection.delete_one({"_id": ObjectId(patient_id)})
    return True


# 🧾 HealthIndicators CRUD
def create_health_indicator(indicator: dict):
    result = health_indicators_collection.insert_one(indicator)
    return str(result.inserted_id)


def get_health_indicator(indicator_id: str):
    return health_indicators_collection.find_one(
        {"_id": ObjectId(indicator_id)}
    )


def update_health_indicator(indicator_id: str, update_data: dict):
    health_indicators_collection.update_one(
        {"_id": ObjectId(indicator_id)}, {"$set": update_data}
    )
    return get_health_indicator(indicator_id)


def delete_health_indicator(indicator_id: str):
    health_indicators_collection.delete_one({"_id": ObjectId(indicator_id)})
    return True
