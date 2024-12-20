from fastapi import FastAPI

from src.users.router import router as users_router
from src.books.router import router as books_router
from src.reviews.router import router as reviews_router


app = FastAPI()

app.include_router(users_router)
app.include_router(books_router)
app.include_router(reviews_router)
