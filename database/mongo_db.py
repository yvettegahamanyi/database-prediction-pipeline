# app/database/mongo.py
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv
import certifi


load_dotenv()

MONGO_URI = os.getenv("MONGO_DATABASE_URL")

if not MONGO_URI:
    raise ValueError(
        "MONGO_DATABASE_URL environment variable is not set. "
        "Please set it in your .env file."
    )

# Create MongoDB client with lazy connection
# Connection will be established on first database operation
# This avoids SSL/TLS handshake errors at application startup
try:
    # Try to create client with ServerApi for MongoDB Atlas compatibility
    # Remove server_api parameter if it causes SSL issues
    client = MongoClient(
        MONGO_URI,
        tlsCAFile=certifi.where(),
        server_api=ServerApi('1'),
        serverSelectionTimeoutMS=20000,  # 20 second timeout
        connectTimeoutMS=20000,
        socketTimeoutMS=20000,
        retryWrites=True,
        retryReads=True,
    )
    db = client["heart_disease_dataset"]
    
    # Optional: Test connection (comment out if causing SSL errors)
    # Uncomment the line below only if you want to test at startup
    # client.admin.command('ping')
    
except Exception as e:
    # If ServerApi causes issues, try without it
    print(f"Warning: MongoDB connection with ServerApi failed: {e}")
    print("Retrying without ServerApi...")
    try:
        client = MongoClient(
            MONGO_URI,
            serverSelectionTimeoutMS=20000,
            connectTimeoutMS=20000,
            socketTimeoutMS=20000,
            retryWrites=True,
            retryReads=True,
        )
        db = client["heart_disease_dataset"]
        print("MongoDB client created successfully (without ServerApi)")
    except Exception as e2:
        print(f"Warning: MongoDB connection failed: {e2}")
        print("Connection will be retried on first database operation.")
        # Create minimal client - will fail on first operation but 
        # allows app to start
        client = MongoClient(MONGO_URI)
        db = client["heart_disease_dataset"]

# collections
patients_collection = db["patients"]
health_indicators_collection = db["health_indicators"]
predictions_collection = db["predictions"]
medical_history_collection = db["medical_history"]
