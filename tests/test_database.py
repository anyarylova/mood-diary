from backend.app.database import get_db
from sqlalchemy import text


def test_get_db_connection():
    gen = get_db()
    db = next(gen)
    assert db is not None
    try:
        db.execute(text("SELECT 1"))
    finally:
        try:
            next(gen)
        except StopIteration:
            pass
