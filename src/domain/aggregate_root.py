from uuid import UUID
from typing import Optional
from src.domain.entity import Entity


class AggregateRoot(Entity):
    """
    Raiz de agregado em Domain-Driven Design.
    
    Um Aggregate Root é responsável por manter a integridade do agregado.
    Apenas o Aggregate Root é acessível de fora do agregado.
    """
    
    def __init__(self, id: Optional[UUID] = None):
        super().__init__(id)