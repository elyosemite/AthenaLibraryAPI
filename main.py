from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items = []

@app.get("/")
def root():
    return { "Hello": "World" }

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items

@app.get("/items")
def get_all_items(limit: int = 10):
    return items[0:limit]

@app.get("/items/{item_id}")
def get_item_by_id(item_id: int) -> str:
    if item_id < len(items):
        return items[items]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
