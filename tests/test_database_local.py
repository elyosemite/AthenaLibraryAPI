from src.infra.book_repository import BookRepository
from src.domain.book import Book
from src.infra.database import metadata, engine

class TestDatabaseLocal:
    def setup_method(self):
        metadata.drop_all(engine)
        metadata.create_all(engine)

    def test_insert_and_select_book(self):
        repo = BookRepository()

        new_book = Book(title="test", description="any")
        inserted = repo.insert(new_book)

        assert inserted.id is not None

        fetched = repo.select(new_book)
        assert fetched is not None
        assert fetched.title == "test"
        assert fetched.description == "any"
