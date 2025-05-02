
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from collections import Counter
from backend.app import models, database
from backend.app.auth_utils import get_current_user

router = APIRouter()


@router.get("/")
def get_stats(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    moods = db.query(models.MoodEntry).filter(
        models.MoodEntry.user_id == current_user.id).all()

    if not moods:
        return {"message": "No mood entries found yet."}

    total_moods = len(moods)
    average_mood = sum(m.mood for m in moods) / total_moods

    # Best and worst day
    best_mood = max(moods, key=lambda x: x.mood)
    worst_mood = min(moods, key=lambda x: x.mood)

    # Most common mood
    mood_counter = Counter(m.mood for m in moods)
    most_common_mood_id, _ = mood_counter.most_common(1)[0]

    mood_labels = {
        0: "😔 Sad",
        1: "🙁 Low",
        2: "🙂 Neutral",
        3: "😊 Happy",
        4: "😄 Excited"
    }
    most_common_mood_label = mood_labels.get(most_common_mood_id, "Unknown")

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
        "most_common_mood": most_common_mood_label
    }
