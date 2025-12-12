from pydantic import BaseModel
from typing import Optional, List

class BookSchema(BaseModel):
    id: int
    title: str
    description: str