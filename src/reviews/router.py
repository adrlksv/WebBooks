from fastapi import APIRouter, Depends

from src.reviews.schemas import SReviewCreate, SReviewUpdate
from src.users.dependencies import get_current_user
from src.reviews.dao import ReviewsDAO
from src.books.dao import BooksDAO

from src.exceptions import (ReviewCreateFailedException, BookNotFoundException, 
                            ReviewGetException, ReviewNotFoundException, NotAbleToUpdateException)


router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"]
)


@router.post("", summary="Endpoint for review creation")
async def create_review(review: SReviewCreate, user = Depends(get_current_user)):
    try:
        return await ReviewsDAO.create_review(review, user)
    except Exception:
        raise ReviewCreateFailedException
    

@router.get("/{book_id}", description="Description")
async def get_reviews_for_book(book_id: int, user = Depends(get_current_user)):
    try:
        book = await BooksDAO.get_book(book_id)

        if not book:
            raise BookNotFoundException
        
        return await ReviewsDAO.get_reviews_for_book(book_id)
    except Exception:
        raise ReviewGetException
    

@router.put("/{review_id}", response_description="Response contains message about results")
async def update_review(
    review_id: int,
    updated_review: SReviewUpdate,
    user = Depends(get_current_user),
):
    current_review = await ReviewsDAO.get_review(review_id)
    review = current_review

    if not current_review:
        raise ReviewNotFoundException
    
    if review.user_id != user.id:
        raise NotAbleToUpdateException
    
    await ReviewsDAO.update_reviews(review_id, **updated_review.model_dump())
    
    return {
        "message": "Review updated successfully !"
    }


@router.delete("/{review_id}")
async def delete_review(review_id: int, user = Depends(get_current_user)):
    current_review = await ReviewsDAO.get_review(review_id)

    if not current_review:
        raise ReviewNotFoundException
    
    return await ReviewsDAO.delete_review(review_id, user)
