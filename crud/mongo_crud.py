from database.mongo_db import (
    patients_collection,
    health_indicators_collection,
    medical_history_collection,
)
from bson import ObjectId
from bson.errors import InvalidId
from pymongo.errors import ServerSelectionTimeoutError, ConnectionFailure
from fastapi import HTTPException


def convert_objectid_to_str(obj):
    """Convert ObjectId to string in MongoDB documents."""
    if obj is None:
        return None
    if isinstance(obj, list):
        return [convert_objectid_to_str(item) for item in obj]
    if isinstance(obj, dict):
        result = {}
        for key, value in obj.items():
            if isinstance(value, ObjectId):
                result[key] = str(value)
            elif isinstance(value, (dict, list)):
                result[key] = convert_objectid_to_str(value)
            else:
                result[key] = value
        return result
    if isinstance(obj, ObjectId):
        return str(obj)
    return obj


#  Patients CRUD
def create_patient(patient: dict):
    try:
        result = patients_collection.insert_one(patient)
        return str(result.inserted_id)
    except (ServerSelectionTimeoutError, ConnectionFailure) as e:
        raise HTTPException(
            status_code=503,
            detail=f"MongoDB connection failed: {str(e)}. "
                   "Please check your MongoDB connection string and network."
        )


def get_patient(patient_id: str):
    try:
        patient = patients_collection.find_one({"_id": ObjectId(patient_id)})
        return convert_objectid_to_str(patient)
    except (ServerSelectionTimeoutError, ConnectionFailure) as e:
        raise HTTPException(
            status_code=503,
            detail=f"MongoDB connection failed: {str(e)}"
        )


def get_patient_by_id(patient_id: str):
    patient = patients_collection.find_one({"_id": ObjectId(patient_id)})
    return convert_objectid_to_str(patient)


def delete_patient(patient_id: str):
    patients_collection.delete_one({"_id": ObjectId(patient_id)})
    return True


def get_all_patients():
    patients = list(patients_collection.find())
    return convert_objectid_to_str(patients)


def update_patient(patient_id: str, update_data: dict):
    patients_collection.update_one(
        {"_id": ObjectId(patient_id)}, {"$set": update_data}
    )
    return get_patient(patient_id)  # Already converts ObjectId


def delete_patient(patient_id: str):
    patients_collection.delete_one({"_id": ObjectId(patient_id)})
    return True


#  HealthIndicators CRUD
def create_health_indicator(patient_id: str, indicator: dict):
    try:
        # Validate patient_id is a valid ObjectId
        try:
            patient_object_id = ObjectId(patient_id)
        except (InvalidId, TypeError):
            raise HTTPException(
                status_code=400,
                detail=f"Invalid patient_id format: {patient_id}"
            )
        
        # Check if patient exists
        patient = patients_collection.find_one({"_id": patient_object_id})
        if not patient:
            raise HTTPException(
                status_code=404,
                detail=f"Patient with ID {patient_id} not found"
            )
        
        result = health_indicators_collection.insert_one(
            {**indicator, "patient_id": patient_object_id}
        )
        return str(result.inserted_id)
    except HTTPException:
        raise
    except (ServerSelectionTimeoutError, ConnectionFailure) as e:
        raise HTTPException(
            status_code=503,
            detail=f"MongoDB connection failed: {str(e)}. "
                   "Please check your MongoDB connection string and network."
        )


def get_health_indicator(indicator_id: str):
    indicator = health_indicators_collection.find_one(
        {"_id": ObjectId(indicator_id)}
    )
    return convert_objectid_to_str(indicator)


def update_health_indicator(indicator_id: str, update_data: dict):
    health_indicators_collection.update_one(
        {"_id": ObjectId(indicator_id)}, {"$set": update_data}
    )
    return get_health_indicator(indicator_id)  # Already converts ObjectId


def delete_health_indicator(indicator_id: str):
    health_indicators_collection.delete_one({"_id": ObjectId(indicator_id)})
    return True

# MedicalHistory CRUD

def create_medical_history(patient_id: str, history: dict):
    try:
        # Validate patient_id is a valid ObjectId
        try:
            patient_object_id = ObjectId(patient_id)
        except (InvalidId, TypeError):
            raise HTTPException(
                status_code=400,
                detail=f"Invalid patient_id format: {patient_id}"
            )
        
        # Check if patient exists
        patient = patients_collection.find_one({"_id": patient_object_id})
        if not patient:
            raise HTTPException(
                status_code=404,
                detail=f"Patient with ID {patient_id} not found"
            )
        
    except (InvalidId, TypeError):
        raise HTTPException(
            status_code=400,
            detail=f"Invalid patient_id format: {patient_id}"
        )
    result = medical_history_collection.insert_one(
        {**history, "patient_id": patient_object_id}
    )
    return str(result.inserted_id)


def get_medical_history(history_id: str):
    history = medical_history_collection.find_one({"_id": ObjectId(history_id)})
    return convert_objectid_to_str(history)


def get_all_medical_histories():
    histories = list(medical_history_collection.find())
    return convert_objectid_to_str(histories)

def update_medical_history(history_id: str, update_data: dict):
    medical_history_collection.update_one(
        {"_id": ObjectId(history_id)}, {"$set": update_data}
    )
    return get_medical_history(history_id)  # Already converts ObjectId

def delete_medical_history(history_id: str):
    medical_history_collection.delete_one({"_id": ObjectId(history_id)})
    return True

