from fastapi import HTTPException, status


class BaseException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)

class TokenExpiredException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "The token has expired"

class TokenAbsentException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "The token is missing"

class IncorrectTokenFormatException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect token format"

class UserIsNotPresentException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = ""

class UserAlreadyExistsException(BaseException):
    status_code = status.HTTP_409_CONFLICT
    detail = "User already exists"

class IncorrectEmailOrPasswordException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect email or password"

class BookNotFoundException(BaseException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Book not found"

class FileNotFoundException(BaseException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "File not found"

class BookUploadException(BaseException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Book upload error"
