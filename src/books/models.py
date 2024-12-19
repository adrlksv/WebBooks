from sqlalchemy import Column, Integer, String

from src.database import Base


class Books(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200))
    author = Column(String(100))
    description = Column(String)
    link = Column(String(50))

    class Config:
        orm_mode = True
