from fastapi import Form, File, UploadFile

import os

from sqlalchemy import select, delete, insert, update

from src.database import async_session_maker
from src.dao.base import BaseDAO
from src.books.models import Books
from src.exceptions import BookNotFoundException, FileNotFoundException

from starlette.responses import FileResponse


UPLOAD_FOLDER = "src/uploaded_books"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


class BooksDAO(BaseDAO):
    model = Books

    @classmethod
    async def upload_book(
        cls,
        title = Form(...),
        author = Form(...),
        description = Form(...),
        file: UploadFile = File(...)
    ):
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(file_path, "wb") as buffer:
            contents = await file.read()
            buffer.write(contents)
        
        async with async_session_maker() as session:
            query = insert(Books).values(
                title=title,
                author=author,
                description=description,
                link=file_path,
            )
            await session.execute(query)
            await session.commit()

            return {
                "title": title,
                "author": author,
                "description": description,
                "link": file_path,
                "BOOK CREATED": "SUCCESSFULLY"
            }
        
    @classmethod
    async def get_book(
        cls,
        book_id: int,
    ):
        async with async_session_maker() as session:
            query = select(Books).where(Books.id == book_id)
            found_book = await session.execute(query)
            book = found_book.scalar_one_or_none()
            
            download_link = f"/books/download/{book_id}"

            return {
                "title": book.title,
                "author": book.author,
                "description": book.description,
                "link": download_link
            }
        
    @classmethod
    async def download_book(
        cls,
        book_id: int
    ):
        async with async_session_maker() as session:
            query = select(Books).where(Books.id == book_id)
            found_book = await session.execute(query)
            book = found_book.scalar_one_or_none()

            if not book:
                raise BookNotFoundException
            
            file_path = book.link

            if not os.path.exists(file_path):
                raise FileNotFoundException
            
            return FileResponse(path=file_path, filename=os.path.basename(file_path))
        
    @classmethod
    async def delete_book(
        cls,
        book_id: int
    ):
        async with async_session_maker() as session:
            query = delete(Books).where(Books.id == book_id)
            await session.execute(query)
            await session.commit()

            return {
                "message": "Book deleted successfully"
            }
        
    @classmethod
    async def update_book(
        cls,
        book_id: int,
        **data,  
    ):
        async with async_session_maker() as session:
            query = update(Books).where(Books.id == book_id).values(**data)
            book = await session.execute(query)
            await session.commit()

            return book
