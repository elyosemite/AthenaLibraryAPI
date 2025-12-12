from uuid import UUID
from typing import Optional
from src.domain.aggregate_root import AggregateRoot


class Order(AggregateRoot):
    """Order é o Aggregate Root do agregado Order"""
    
    def __init__(self, id: Optional[UUID] = None, customer_name: str = ""):
        super().__init__(id)
        self.customer_name = customer_name

    @classmethod
    def restore_from_database(cls, **kwargs):
        """Restaura Order a partir dos dados do banco"""
        return super().restore_from_database(**kwargs)
