from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.infra.book_schema import BookSchema

app = FastAPI()

books = []

@app.get("/")
def root():
    return { "Hello": "World" }

@app.post("/book")
def create_item(book: BookSchema):
    books.append(book)
    return books

@app.get("/books", response_model=list[BookSchema])
def get_all_books(limit: int = 10):
    return books[0:limit]

@app.get("/books/{book_id}", response_model=BookSchema)
def get_item_by_id(book_id: int) -> BookSchema:
    if book_id < len(books):
        return books[book_id]
    else:
        raise HTTPException(status_code=404, detail=f"Book {book_id} not found")
