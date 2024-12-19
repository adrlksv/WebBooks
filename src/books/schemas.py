from pydantic import BaseModel, Field

from typing import Optional


class SBooks(BaseModel):
    title: str = Field(..., description="Заголовое книги")
    author: str = Field(..., description="Автор книги")
    description: Optional[str] = Field("Нет описания", description="Описание книги")
