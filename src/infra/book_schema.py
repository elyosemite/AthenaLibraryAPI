from pydantic import BaseModel
from typing import Optional, List

class BookSchema(BaseModel):
    title: str
    description: str
    authors: List[str] = []

    class Config:
        from_attributes = True