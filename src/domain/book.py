from typing import Optional, List

class Book():
    def __init__(self, title: str, description: str, authors: Optional[List['Author']] = None):
        self.title = title
        self.description = description
        self.authors = authors or []
    
    def has_authors(self) -> bool:
        return len(self.authors) > 0