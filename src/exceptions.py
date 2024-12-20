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

class NoDataToUpdateException(BaseException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "No data to update"

class InternalServerErrorException(BaseException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Internal server error"

class ReviewCreateFailedException(BaseException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Review create failed"

class ReviewGetException(BaseException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Failed to get review"

class ReviewNotFoundException(BaseException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Review not found"

class NotAbleToUpdateException(BaseException):
    status_code = status.HTTP_409_CONFLICT
    detail = "You are not able to update this review"
