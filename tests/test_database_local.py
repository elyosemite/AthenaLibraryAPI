from src.infra.book_repository import BookRepository
from src.domain.book import Book
from src.infra.database import metadata, engine

class TestDatabaseLocal:
    def setup_method(self):
        metadata.drop_all(engine)
        metadata.create_all(engine)

    def test_insert_and_select_book(self):
        repo = BookRepository()
        book_title = "Microservice Patterns: With examples in Java"
        book_description = "44 reusable patterns to develop and deploy reliable production-quality microservices-based applications, with worked examples in Java"

        new_book = Book(title=book_title, description=book_description)
        inserted = repo.insert(new_book)

        assert inserted.id is not None

        fetched = repo.select(new_book)
        assert fetched is not None
        assert fetched.title == book_title
        assert fetched.description == book_description
