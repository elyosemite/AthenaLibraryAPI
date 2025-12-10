class Author:
    def __init__(self, name: str):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book);