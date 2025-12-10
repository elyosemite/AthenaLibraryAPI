from src.domain.author import Author
from src.domain.book import Book

class TestAuthor:
    def test_create_author(self):
        author = Author("J. K. Rowling")
        assert author.name == "J. K. Rowling"
        assert author.books == []

    def test_add_single_book(self):
        author = Author("George Orwell")
        book = Book("1984", "Dystopian novel")

        author.add_book(book)

        assert len(author.books) == 1
        assert author.books[0] == book
    
    def test_add_multiple_books(self):
        author = Author("Isaac Asimov")
        book1 = Book("Foundation", "Science fiction")
        book2 = Book("I, Robot", "Robot stories")
        
        author.add_book(book1)
        author.add_book(book2)
        
        assert len(author.books) == 2
        assert book1 in author.books
        assert book2 in author.books
    
    def test_books_list_initially_empty(self):
        author = Author("Test Author")
        assert isinstance(author.books, list)
        assert len(author.books) == 0