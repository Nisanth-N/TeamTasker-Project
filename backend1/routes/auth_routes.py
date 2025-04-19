from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from utils.hashing import hash_password, verify_password
from database.mongo import user_collection

auth_router = APIRouter()

class SignupRequest(BaseModel):
    username: str
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

@auth_router.post("/signup")
async def signup(request: SignupRequest):
    print("Received signup request:", request)  # Debugging line

    existing_user = await user_collection.find_one({"email": request.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_password = hash_password(request.password)

    new_user = {
        "username": request.username,
        "email": request.email,
        "password": hashed_password
    }

    result = await user_collection.insert_one(new_user)
    return {
        "message": "User created successfully",
        "user_id": str(result.inserted_id)
    }

@auth_router.post("/login")
async def login(request: LoginRequest):
    user = await user_collection.find_one({"email": request.email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(request.password, user["password"]):
        raise HTTPException(status_code=401, detail="Incorrect password")

    return {
        "message": "Login successful",
        "username": user["username"],
        "email": user["email"]
    }
