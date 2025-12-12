from typing import Optional
from sqlalchemy import select

from domain.book import Book
from .database import engine
from .book import book_table # data model

class BookRepository:
    def insert_user(book: Book) -> None:
        query = book_table.insert().values(
            title=book.title,
            description=book.description
        )
        with engine.begin() as conn:
            result = conn.execute(query)
            book.id = result.inserted_primary_key[0]
            return book

    def select_user(book: Book) -> Optional[Book]:
        smtm = select(book_table).where(book_table.c.title == book.title)
        with engine.begin() as conn:
            row = conn.execute(smtm).fetchone()
            if row:
                return Book(id=row.id, title=row.title, description=book.description)
            return None