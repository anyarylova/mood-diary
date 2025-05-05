from fastapi import HTTPException
from pydantic import BaseModel, ConfigDict, Field, field_validator
from datetime import date
import re

USERNAME_REGEX = re.compile(r"^[a-zA-Z0-9_]{3,20}$")


class UserCreate(BaseModel):
    username: str = Field(
        ...,
        description="Username (3-20 alphanumeric characters or underscore)"
    )
    password: str = Field(
        ...,
        min_length=7,
        description="Password (min 7 characters)"
    )

    @field_validator('username')
    def validate_username(cls, v):
        if not USERNAME_REGEX.match(v):
            raise HTTPException(
                status_code=422,
                detail="Username must be 3-20 characters long\
                    and contain only letters, numbers, or underscores"
            )
        return v


class UserLogin(UserCreate):
    pass


class MoodCreate(BaseModel):
    date: date
    mood: int = Field(
        ...,
        ge=0,
        le=4,
        description="Mood rating (0-4)"
    )
    note: str | None = Field(
        None,
        max_length=5000,
        description="Optional note about the mood (max 5000 chars)"
    )


class MoodOut(MoodCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
