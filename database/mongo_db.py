# app/database/mongo.py
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_DATABASE_URL")

client = MongoClient(MONGO_URI)
db = client["heart_disease_dataset"]

# collections
patients_collection = db["patients"]
health_indicators_collection = db["health_indicators"]
predictions_collection = db["predictions"]
medical_history_collection = db["medical_history"]
