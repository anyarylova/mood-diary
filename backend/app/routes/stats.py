from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from collections import Counter
from backend.app import models, database
from backend.app.auth_utils import get_current_user
from backend.app.logger import logger

router = APIRouter()


@router.get("/")
def get_stats(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    moods = db.query(models.MoodEntry).filter(
        models.MoodEntry.user_id == current_user.id).all()

    if not moods:
        logger.info(
            f"Stats requested by user={current_user.username}, "
            "but no entries found."
        )
        return {"message": "No mood entries found yet."}

    total_moods = len(moods)
    average_mood = sum(m.mood for m in moods) / total_moods

    best_mood = max(moods, key=lambda x: x.mood)
    worst_mood = min(moods, key=lambda x: x.mood)

    mood_counter = Counter(m.mood for m in moods)
    most_common_mood_id, _ = mood_counter.most_common(1)[0]

    mood_labels = {
        0: "😔 Sad",
        1: "🙁 Low",
        2: "🙂 Neutral",
        3: "😊 Happy",
        4: "😄 Excited"
    }
    logger.info(
        f"Stats generated for user={current_user.username}, "
        f"entries={total_moods}"
    )
    return {
        "total_moods_logged": total_moods,
        "average_mood_score": round(average_mood, 2),
        "best_day": {
            "date": best_mood.date.isoformat(),
            "mood": mood_labels.get(best_mood.mood, "Unknown"),
            "note": best_mood.note
        },
        "worst_day": {
            "date": worst_mood.date.isoformat(),
            "mood": mood_labels.get(worst_mood.mood, "Unknown"),
            "note": worst_mood.note
        },
        "most_common_mood": mood_labels.get(most_common_mood_id, "Unknown")
    }
