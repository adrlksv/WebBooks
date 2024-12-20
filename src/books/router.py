from fastapi import APIRouter, Depends, File, Form, UploadFile

from src.books.dao import BooksDAO
from src.users.dependencies import get_current_user
from src.exceptions import BookNotFoundException, BookUploadException, InternalServerErrorException


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
    try:
        book = await BooksDAO.upload_book(title, author, description, file)

        if not book:
            raise BookUploadException
    except Exception:
        raise InternalServerErrorException


@router.get("/get-book/{book_id}")
async def get_book(book_id: int, user = Depends(get_current_user)):
    try:
        book = await BooksDAO.get_book(book_id)

        if not book:
            raise BookNotFoundException
        
        return book
    except Exception:
        raise InternalServerErrorException


@router.get("/download-book/{book_id}")
async def download_book(
    book_id: int,
    user = Depends(get_current_user)
):
    try:
        found_book = await BooksDAO.get_book(book_id)

        if not found_book:
            raise BookNotFoundException
        
        return await BooksDAO.download_book(book_id)
    except Exception:
        raise InternalServerErrorException


@router.put("/update-book/{book_id}")
async def update_book(
    book_id: int,
    title = Form(...),
    author = Form(...),
    description = Form(...),
    user = Depends(get_current_user),
):
    try:
        found_book = await BooksDAO.get_book(book_id)

        if not found_book:
            raise BookNotFoundException
        
        return await BooksDAO.update_book(book_id, title, author, description)
    except Exception:
        raise InternalServerErrorException


@router.delete("/delete-book/{book_id}")
async def delete_book(
    book_id: int,
    user = Depends(get_current_user)
):
    try:
        found_book = await BooksDAO.get_book(book_id)

        if not found_book:
            raise BookNotFoundException
        
        return await BooksDAO.delete_book(book_id)
    except Exception:
        raise InternalServerErrorException
