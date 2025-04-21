from pydantic import BaseModel
from datetime import date

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(UserCreate):
    pass

class MoodCreate(BaseModel):
    date: date
    mood: int
    note: str | None = None

class MoodOut(MoodCreate):
    id: int

    class Config:
        orm_mode = True
