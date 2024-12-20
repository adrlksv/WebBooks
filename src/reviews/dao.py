from sqlalchemy import select, insert, update, delete

from src.database import async_session_maker
from src.reviews.models import Reviews
from src.dao.base import BaseDAO

from datetime import datetime


class ReviewsDAO(BaseDAO):
    model = Reviews

    @classmethod
    async def create_review(cls, review, user):
        async with async_session_maker() as session:
            query = insert(Reviews).values(
                user_id=user.id,
                book_id=review.book_id,
                rating=review.rating,
                review_text=review.review_text,
                created_at=datetime.utcnow()
            )

            await session.execute(query)
            await session.commit()

            return {
                "message": "Review added successfully !"
            }
        
    @classmethod
    async def get_review(cls, review_id):
        async with async_session_maker() as session:
            query = select(Reviews).where(Reviews.id == review_id)
            result = await session.execute(query)

            return result.scalar_one_or_none()
    
    @classmethod
    async def get_reviews_for_book(cls, book_id):
        async with async_session_maker() as session:
            query = select(Reviews).where(Reviews.book_id == book_id)
            result = await session.execute(query)
            
            return result.scalars().all()
        
    @classmethod
    async def update_reviews(cls, review_id, **updated_review):
        async with async_session_maker() as session:
            query = update(Reviews).where(Reviews.id == review_id).values(
                review_text=updated_review.get("review_text"),
                rating=updated_review.get("rating")
            )

            await session.execute(query)
            await session.commit()

            return {
                "message": "Review updated successfully !"
            }
        
    @classmethod
    async def delete_review(cls, review_id, user):
        async with async_session_maker() as session:
            query = delete(Reviews).where(Reviews.id == review_id)

            await session.execute(query)
            await session.commit()

            return {
                "message": "Review deleted successfully !"
            }
