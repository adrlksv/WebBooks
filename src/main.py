from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.users.router import router as users_router
from src.books.router import router as books_router
from src.reviews.router import router as reviews_router


app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:3000/register",
    "http://localhost:3000/login",
    "http://localhost:3000/add-book",
    "http://localhost:3000/profile"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "UPDATE", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(books_router)
app.include_router(reviews_router)
