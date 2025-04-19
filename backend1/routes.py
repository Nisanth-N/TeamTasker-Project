from fastapi import APIRouter, HTTPException, Depends
from models import User
from database import users_collection
from passlib.context import CryptContext
import jwt
import os

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "your_secret_key"

# Signup Route
@router.post("/signup")
async def signup(user: User):
    existing_user = await users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_password = pwd_context.hash(user.password)
    new_user = { "username": user.username, "email": user.email, "password": hashed_password }
    
    await users_collection.insert_one(new_user)
    return {"message": "User registered successfully"}

# Login Route
@router.post("/login")
async def login(user: User):
    stored_user = await users_collection.find_one({"email": user.email})
    if not stored_user or not pwd_context.verify(user.password, stored_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = jwt.encode({"user_id": str(stored_user["_id"])}, SECRET_KEY, algorithm="HS256")
    return {"message": "Login successful", "token": token}

from models import User, Task
from database import users_collection, tasks_collection

# Add Task to DB
@router.post("/add-task")
async def add_task(task: Task):
    task_dict = task.dict()
    result = await tasks_collection.insert_one(task_dict)
    if result.inserted_id:
        return {"message": "Task added successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to add task")

# Get Tasks for a User
@router.get("/get-tasks/{user_id}")
async def get_tasks(user_id: str):
    tasks = await tasks_collection.find({"user_id": user_id}).to_list(length=100)
    return tasks
