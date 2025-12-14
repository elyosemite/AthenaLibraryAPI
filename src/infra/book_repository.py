from typing import Optional
from sqlalchemy import select

from src.domain.book import Book
from src.infra.book_schema import BookSchema
from .database import engine
from .book import book_table
from .author import author_table
from .book_author import book_author_table

class BookRepository:
    def insert(self, book: Book) -> None:

        # Insert a book
        bookQuery = book_table.insert().values(
            id=str(book.id),
            title=book.title,
            description=book.description
        )

        authors_data = [
            { "name": author.name } for author in book.authors
        ]

        # If there is a authors, so insert them
        authorQuery = author_table.insert().values(authors_data)

        with engine.begin() as conn:
            bookResult = conn.execute(bookQuery)
            authorResult = conn.execute(authorQuery)
            
            bookId = bookResult.inserted_primary_key[0]
            authorId = authorResult.inserted_primary_key[0]

            # If there is a authors, so bind them to book (many-to-many)
            book_author_query = book_author_table.insert().values(
                book_id=bookId,
                author_id=authorId
            )

            return Book(bookId, book.title, book.description)

    def select(self, book: Book) -> Optional[Book]:
        smtm = select(book_table).where(book_table.c.title == book.title)
        with engine.begin() as conn:

            row = conn.execute(smtm).fetchone()
            if row:
                schema = BookSchema(id=row.id, title=row.title, description=book.description)
                return Book(schema.title, schema.description)
            return None