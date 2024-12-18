from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from src.database import Base

from datetime import datetime


class Reviews(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
    rating = Column(Integer)
    review_text = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
