from abc import ABC, abstractmethod
from typing import List
from domain.book import Book

class BookRepository(ABC):

    @abstractmethod
    async  def get_book_by_id(self, user_id: int) -> Book | None:
        pass

    @abstractmethod
    async def create(self, book: Book) -> Book:
        pass

    @abstractmethod
    async def list_all(self) -> List[Book]:
        pass