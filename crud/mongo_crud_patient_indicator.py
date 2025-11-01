from app.database.mongo import patients_collection, health_indicators_collection, predictions_collection
from bson import ObjectId

# 🧍 Patients CRUD
async def create_patient(patient: dict):
    result = await patients_collection.insert_one(patient)
    return str(result.inserted_id)

async def get_patient(patient_id: str):
    return await patients_collection.find_one({"_id": ObjectId(patient_id)})

async def get_all_patients():
    return [p async for p in patients_collection.find()]

async def update_patient(patient_id: str, update_data: dict):
    await patients_collection.update_one({"_id": ObjectId(patient_id)}, {"$set": update_data})
    return await get_patient(patient_id)

async def delete_patient(patient_id: str):
    await patients_collection.delete_one({"_id": ObjectId(patient_id)})
    return True