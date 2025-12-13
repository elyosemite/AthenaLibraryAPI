from typing import Optional, List
from uuid import UUID

from src.domain.aggregate_root import AggregateRoot
from src.domain.author import Author

class Book(AggregateRoot):
    def __init__(self, title: str, description: str, authors: Optional[List[Author]] = None):
        super().__init__()
        self.title = title
        self.description = description
        self.authors = authors or []
    
    def has_authors(self) -> bool:
        return len(self.authors) > 0
    
    def add_author(self, author: Author):
        self.authors.append(author)
    
    @classmethod
    def restore_from_database(cls, **kwargs):
        return super().restore_from_database(**kwargs)