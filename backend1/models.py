from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    username: str
    email: EmailStr
    password: str

class Task(BaseModel):
    user_id: str
    title: str
    description: Optional[str] = ""
    date: str
    time: str