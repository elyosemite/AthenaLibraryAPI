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

        with engine.begin() as conn:
            # Insert a book
            bookQuery = book_table.insert().values(
                id=str(book.id),
                title=book.title,
                description=book.description
            )
            conn.execute(bookQuery)

            # insert Author
            authors_data = [
                { "name": author.name } for author in book.authors
            ]

            # If there is a authors, so insert them
            authorQuery = (
                author_table
                .insert()
                .values(authors_data)
                .returning(author_table.c.id) # is just work in POstgreSQL and SQLite 3
            )

            author_ids = conn.execute(authorQuery).scalars().all()
            
            book_author_data = [
                {
                    "book_id": str(book.id),
                    "author_id": author_id
                }
                for author_id in author_ids
            ]

            conn.execute(
                book_author_table.insert().values(book_author_data)
            )

    def select(self, book: Book) -> Optional[Book]:
        smtm = select(book_table).where(book_table.c.title == book.title)
        with engine.begin() as conn:

            row = conn.execute(smtm).fetchone()
            if row:
                schema = BookSchema(id=row.id, title=row.title, description=book.description)
                return Book(schema.title, schema.description)
            return None