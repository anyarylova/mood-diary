from pydantic import BaseModel, ConfigDict
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
    model_config = ConfigDict(from_attributes=True)
