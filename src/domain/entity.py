from uuid import UUID, uuid4
from typing import Optional

class Entity:
    def __init__(self, id: Optional[UUID] = None):
        self._id = id if id is not None else uuid4()

    @property
    def id(self) -> UUID:
        return self._id

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Entity):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id})"

    @classmethod
    def restore_from_database(cls, **kwargs):
        """
        Restaura uma entidade a partir dos dados do banco de dados.
        
        Espera 'id' como um dos argumentos (UUID ou string).
        Subclasses podem sobrescrever para adicionar lógica customizada.
        
        Args:
            **kwargs: Dados da entidade (deve incluir 'id')
        
        Returns:
            Uma instância da entidade
        """
        if 'id' not in kwargs:
            raise ValueError(f"{cls.__name__} requer 'id' para ser restaurado do banco de dados")
        
        # Converte string para UUID se necessário
        if isinstance(kwargs['id'], str):
            kwargs['id'] = UUID(kwargs['id'])
        
        return cls(**kwargs)
    