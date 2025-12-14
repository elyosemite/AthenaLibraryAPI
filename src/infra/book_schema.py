from pydantic import BaseModel

class BookSchema(BaseModel):
    id: str
    title: str
    description: str

class AuthorSchema(BaseModel):
    id: str
    name: str

class BookAuthorSchema(BaseModel):
    id: int
    book_id: str
    author_id: str
