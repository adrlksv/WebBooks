from pydantic import BaseModel


class SReviewCreate(BaseModel):
    book_id: int
    rating: int
    review_text: str


class SReviewUpdate(BaseModel):
    rating: int
    review_text: str
