from datetime import datetime
from fastapi import Request, Depends
from jose import jwt, JWTError

from src.config import SECRET_KEY, ENCRYPT

from src.users.dao import UsersDAO
from src.exceptions import (TokenAbsentException, IncorrectTokenFormatException,
                            TokenExpiredException, UserIsNotPresentException)


def get_token(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, SECRET_KEY, ENCRYPT
        )
    except JWTError:
        raise IncorrectTokenFormatException
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < int(datetime.utcnow().timestamp())):
        raise TokenExpiredException
    user_id: str = payload.get("sub")
    if not user_id:
        raise UserIsNotPresentException
    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise UserIsNotPresentException
    
    return user