from sqlalchemy import Column, String, Integer, Enum

from src.database import Base

import enum


class UserRole(enum.Enum):
    user = "user"
    admin = "admin"
    approved_user = "approved_user"


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String)
    role = Column(Enum(UserRole), default=UserRole.user.value)

    class Config:
        orm_mode = True
