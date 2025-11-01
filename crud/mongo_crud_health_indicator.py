# app/crud/mongo_crud.py
from app.database.mongo import health_indicators_collection
from bson import ObjectId


async def create_health_indicator(indicator: dict):
    result = await health_indicators_collection.insert_one(indicator)
    return str(result.inserted_id)

async def get_health_indicator(indicator_id: str):
    return await health_indicators_collection.find_one({"_id": ObjectId(indicator_id)})

async def update_health_indicator(indicator_id: str, update_data: dict):
    await health_indicators_collection.update_one({"_id": ObjectId(indicator_id)}, {"$set": update_data})
    return await get_health_indicator(indicator_id)

async def delete_health_indicator(indicator_id: str):
    await health_indicators_collection.delete_one({"_id": ObjectId(indicator_id)})
    return True