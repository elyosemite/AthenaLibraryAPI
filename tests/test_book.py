from src.domain.book import Book
from src.domain.author import Author

class TestBook:
    def test_Create_book_without_authors(self):
        book = Book("1984", "Dystopian novel")
        assert book.title == "1984"
        assert book.description == "Dystopian novel"
        assert book.authors == []
        assert not book.has_authors()
    
    def test_create_book_with_none_authors(self):
        book = Book("Brave New World", "Dystopian novel", None)
        assert book.authors == []
        assert not book.has_authors()
    
    def test_create_book_with_single_author(self):
        author = Author("George Orwell")
        book = Book("1984", "Dystopian novel", [author])
        
        assert len(book.authors) == 1
        assert book.authors[0] == author
        assert book.has_authors()
    
    def test_create_book_with_multiple_authors(self):
        author1 = Author("Andy Weir")
        author2 = Author("Co-Author Name")
        book = Book("The Martian", "Science fiction", [author1, author2])
        
        assert len(book.authors) == 2
        assert author1 in book.authors
        assert author2 in book.authors
        assert book.has_authors()
    
    def test_create_book_with_empty_list(self):
        book = Book("Test Book", "Test description", [])
        assert book.authors == []
        assert not book.has_authors()
    
    def test_has_authors_returns_true_when_authors_exist(self):
        author = Author("Isaac Asimov")
        book = Book("Foundation", "Sci-fi classic", [author])
        assert book.has_authors() is True
    
    def test_has_authors_returns_false_when_no_authors(self):
        book = Book("Anonymous Book", "No author")
        assert book.has_authors() is False
    
    def test_book_attributes_are_strings(self):
        book = Book("Title", "Description")
        assert isinstance(book.title, str)
        assert isinstance(book.description, str)
    
    def test_authors_is_list(self):
        book = Book("Test", "Test")
        assert isinstance(book.authors, list)