from uuid import UUID
from typing import Optional
from src.domain.entity import Entity

class AggregateRoot(Entity):
    def __init__(self, id: Optional[UUID] = None):
        super().__init__(id)
