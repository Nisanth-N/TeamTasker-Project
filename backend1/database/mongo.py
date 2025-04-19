import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

# Load environment variables from .env file
load_dotenv()

# Set these in your .env file for better security
MONGODB_URI = os.getenv("MONGODB_URI") or "mongodb+srv://nisanthisin:nisanth999@cluster0.rdyvnm6.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = os.getenv("DATABASE_NAME") or "Teamtask"

# Mongo client setup
client = AsyncIOMotorClient(MONGODB_URI)
db = client[DATABASE_NAME]

# Collection reference
user_collection = db["users"]
task_collection = db["tasks"]