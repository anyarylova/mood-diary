from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app import models, schemas, database

router = APIRouter()

# Temporary: fake user auth
def get_fake_user_id():
    return 1  # Hardcoded user ID for now until real auth

@router.post("/", response_model=schemas.MoodOut)
def create_mood_entry(
    mood: schemas.MoodCreate,
    db: Session = Depends(database.get_db)
):
    user_id = get_fake_user_id()

    # Check for duplicate entry for today
    existing = db.query(models.MoodEntry).filter(
        models.MoodEntry.date == mood.date,
        models.MoodEntry.user_id == user_id
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Mood for this date already exists.")

    entry = models.MoodEntry(**mood.dict(), user_id=user_id)
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry

@router.get("/", response_model=list[schemas.MoodOut])
def get_mood_entries(
    db: Session = Depends(database.get_db)
):
    user_id = get_fake_user_id()
    moods = db.query(models.MoodEntry).filter(models.MoodEntry.user_id == user_id).order_by(models.MoodEntry.date.desc()).all()
    return moods
