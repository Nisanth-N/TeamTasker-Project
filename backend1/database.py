from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get MongoDB connection URI from .env
MONGO_URI = "mongodb+srv://nisanthisin:nisanth999@<cluster-url>.mongodb.net/?retryWrites=true&w=majority"

# Initialize MongoDB client
client = AsyncIOMotorClient(MONGO_URI)
db = client["teamtasker_db"]  # Replace with your actual DB name
collection = db["tasks"]  # Replace with your collection name
