from fastapi import FastAPI, HTTPException
from src.infra.book_schema import BookSchema

app = FastAPI()

books = []

@app.post("/book")
def create_book(book: BookSchema):
    books.append(book)
    return books

@app.get("/books", response_model=list[BookSchema])
def get_all_books(limit: int = 10):
    return books[0:limit]

@app.get("/books/{book_id}", response_model=BookSchema)
def get_book_by_id(book_id: int) -> BookSchema:
    if book_id < len(books):
        return books[book_id]
    else:
        raise HTTPException(status_code=404, detail=f"Book {book_id} not found")

@app.delete("/books/{book_id}")
def delete_book_by_id(book_id: int):
    return books[book_id]