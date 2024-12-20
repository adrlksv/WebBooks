from fastapi import APIRouter, Response

from src.users.dao import UsersDAO
from src.users.schemas import SUserCreate, SUserAuthorize

from src.exceptions import UserAlreadyExistsException, IncorrectEmailOrPasswordException, InternalServerErrorException

from src.users.auth import create_access_token, get_password_hash, authenticate_user


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("/register")
async def create_user(user_data: SUserCreate):
    try:
        existing_user = await UsersDAO.find_one_or_none(email=user_data.email)

        if existing_user:
            raise UserAlreadyExistsException
        hashed_password = get_password_hash(user_data.password)
        await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)
    except Exception:
        raise InternalServerErrorException


@router.post("/login")
async def authorize_user(response: Response, user_data: SUserAuthorize):
    try:
        user = await authenticate_user(user_data.email, user_data.password)
        if not user:
            raise IncorrectEmailOrPasswordException
        access_token = create_access_token({"sub": str(user.id)})
        response.set_cookie("access_token", access_token, httponly=True)
        return access_token
    except Exception:
        raise InternalServerErrorException

@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("access_token")
