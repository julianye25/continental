from abc import ABC, abstractmethod
from typing import List, Optional
from ..domain.entities.Client import Cliente


class ClienteRepository(ABC):

    @abstractmethod
    async def create(self, cliente: Cliente) -> Cliente:
        pass

    @abstractmethod
    async def get_by_id(self, cliente_id: str) -> Optional[Cliente]:
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> Optional[Cliente]:
        pass

    @abstractmethod
    async def get_by_documento(self, documento: str) -> Optional[Cliente]:
        pass

    @abstractmethod
    async def get_all(self, limit: int = 100, offset: int = 0) -> List[Cliente]:
        pass

    @abstractmethod
    async def search_by_name(self, name: str) -> List[Cliente]:
        pass

    @abstractmethod
    async def update(self, cliente: Cliente) -> Cliente:
        pass

    @abstractmethod
    async def delete(self, cliente_id: str) -> bool:
        pass

    @abstractmethod
    async def exists_by_email(self, email: str) -> bool:
        pass
