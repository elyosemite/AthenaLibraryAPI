from typing import Optional
from sqlalchemy import select

from src.domain.book import Book
from src.infra.book_schema import BookSchema
from .database import engine
from .book import book_table

class BookRepository:
    def insert(self, book: Book) -> None:
        query = book_table.insert().values(
            title=book.title,
            description=book.description
        )
        with engine.begin() as conn:
            result = conn.execute(query)
            book.id = result.inserted_primary_key[0]
            return book

    def select(self, book: Book) -> Optional[Book]:
        smtm = select(book_table).where(book_table.c.title == book.title)
        with engine.begin() as conn:
            row = conn.execute(smtm).fetchone()
            if row:
                schema = BookSchema(id=row.id, title=row.title, description=book.description)
                return Book(schema.title, schema.description)
            return None