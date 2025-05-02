from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app import models, schemas, database
from backend.app.auth_utils import get_current_user
from backend.app.logger import logger

router = APIRouter()


@router.post("/", response_model=schemas.MoodOut)
def create_mood_entry(
    mood: schemas.MoodCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    user_id = current_user.id

    existing = db.query(models.MoodEntry).filter(
        models.MoodEntry.date == mood.date,
        models.MoodEntry.user_id == user_id
    ).first()
    if existing:
        logger.warning(
            f"Duplicate mood entry rejected for user {current_user.username} "
            f"on {mood.date}"
        )
        raise HTTPException(
            status_code=400, detail="Mood for this date already exists."
        )

    entry = models.MoodEntry(**mood.model_dump(), user_id=user_id)
    db.add(entry)
    db.commit()
    db.refresh(entry)

    logger.info(
        f"Mood logged: user={current_user.username}, "
        f"date={mood.date}, mood={mood.mood}"
    )
    return entry


@router.get("/", response_model=list[schemas.MoodOut])
def get_mood_entries(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    moods = db.query(models.MoodEntry).filter(
        models.MoodEntry.user_id == current_user.id
    ).order_by(models.MoodEntry.date.desc()).all()

    logger.info(
        f"Mood history retrieved: user={current_user.username}, "
        f"entries={len(moods)}"
    )
    return moods
