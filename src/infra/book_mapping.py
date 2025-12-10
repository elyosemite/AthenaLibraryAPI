from src.domain.book import Book
from src.infra.book_schema import BookSchema


class BookMapper:
    @staticmethod
    def to_schema(book: Book) -> BookSchema:
        return BookSchema(
            title=book.title,
            description=book.description,
            authors=[author.name for author in book.authors]
        )

    @staticmethod
    def from_schema(schema: BookSchema) -> Book:
        return Book(
            title=schema.title,
            description=schema.description
        )