from passlib.context import CryptContext
from jwt import encode, decode

from datetime import datetime, timedelta

from pydantic import EmailStr

from typing import Optional

from src.users.dao import UsersDAO
from src.config import SECRET_KEY, ALGORITHM


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = encode(
        to_encode, SECRET_KEY, ALGORITHM
    )
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str) -> Optional[dict]:
    user = await UsersDAO.find_one_or_none(email=email)
    if not user and not verify_password(password, user.password):
        return None
    return user


def decode_access_token(token: str) -> dict:
    try:
        payload = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except Exception as e:
        print(f"Enter decoding token: {e}")
        return None
