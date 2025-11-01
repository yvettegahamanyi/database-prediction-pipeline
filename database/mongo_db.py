# app/database/mongo.py
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING
import os

MONGO_URI = os.getenv("MONGO_URI", "your_mongodb_connection_string_here")

client = AsyncIOMotorClient(MONGO_URI)
db = client["heart_health_db"]

# collections
patients_collection = db["patients"]
health_indicators_collection = db["health_indicators"]
predictions_collection = db["predictions"]
