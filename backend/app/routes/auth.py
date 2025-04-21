from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

users_db = {}

class User(BaseModel):
    username: str
    password: str

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

@router.post("/register")
def register(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    users_db[user.username] = hash_password(user.password)
    return {"msg": "User registered"}

@router.post("/login")
def login(user: User):
    if user.username not in users_db or not verify_password(user.password, users_db[user.username]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"msg": f"Welcome back, {user.username}!"}
