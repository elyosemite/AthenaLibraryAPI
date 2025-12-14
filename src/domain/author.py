from typing import Optional
from uuid import UUID
from src.domain.entity import Entity

class Author(Entity):
    def __init__(self, name: str, id: Optional[UUID] = None):
        super().__init__(id)
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)