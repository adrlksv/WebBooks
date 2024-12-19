from fastapi import APIRouter, Depends, File, Form, UploadFile

from src.books.schemas import SBooks
from src.books.dao import BooksDAO
from src.users.dependencies import get_current_user
from src.exceptions import BookNotFoundException, BookUploadException


router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


@router.post("/create-book")
async def create_book(title = Form(...),
                      author = Form(...),
                      description = Form(...),
                      file: UploadFile = File(...),
                      user = Depends(get_current_user)
                      ):
    book = await BooksDAO.upload_book(title, author, description, file)

    if not book:
        raise BookUploadException


@router.get("/get-book/{book_id}")
async def get_book(book_id: int, user = Depends(get_current_user)):
    book = await BooksDAO.get_book(book_id)

    if not book:
        raise BookNotFoundException
    
    return book


@router.get("/download-book/{book_id}")
async def download_book(
    book_id: int,
    user = Depends(get_current_user)
):
    found_book = await BooksDAO.get_book(book_id)

    if not found_book:
        raise BookNotFoundException
    
    return await BooksDAO.download_book(book_id)


@router.put("/update-book/{book_id}")
async def update_book(
    book_id: int,
    user = Depends(get_current_user),
    **data: SBooks,
):
    found_book = await BooksDAO.get_book(book_id)

    if not found_book:
        raise BookNotFoundException
    
    return await BooksDAO.update_book(book_id)


@router.delete("/delete-book/{book_id}")
async def delete_book(
    book_id: int,
    user = Depends(get_current_user)
):
    found_book = await BooksDAO.get_book(book_id)

    if not found_book:
        raise BookNotFoundException
    
    return await BooksDAO.delete_book(book_id)
