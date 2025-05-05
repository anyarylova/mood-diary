from sqlalchemy import Column, Integer, String, Date, ForeignKey, Index
from sqlalchemy.orm import relationship
from backend.app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    moods = relationship("MoodEntry", back_populates="owner")


class MoodEntry(Base):
    __tablename__ = "mood_entries"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True, nullable=False)
    mood = Column(Integer, nullable=False)
    note = Column(String, nullable=True)

    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    owner = relationship("User", back_populates="moods")

    __table_args__ = (
        Index('ix_mood_entries_user_id_date', 'user_id', 'date'),
    )
