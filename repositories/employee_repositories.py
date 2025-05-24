from abc import ABC, abstractmethod
from typing import List, Optional
from ..domain.entities.employee import Empleado, TipoEmpleado, EstadoEmpleado



class EmpleadoRepository(ABC):
    
    @abstractmethod
    async def create(self, empleado: Empleado) -> Empleado:
        pass
    
    @abstractmethod
    async def get_by_id(self, empleado_id: str) -> Optional[Empleado]:
        pass
    
    @abstractmethod
    async def get_by_email(self, email: str) -> Optional[Empleado]:
        pass
    
    @abstractmethod
    async def get_by_documento(self, documento: str) -> Optional[Empleado]:
        pass
    
    @abstractmethod
    async def get_all(self, limit: int = 100, offset: int = 0) -> List[Empleado]:
        pass
    
    @abstractmethod
    async def get_by_tipo(self, tipo: TipoEmpleado) -> List[Empleado]:
        pass
    
    @abstractmethod
    async def get_by_turno(self, turno: str) -> List[Empleado]:
        pass
    
    @abstractmethod
    async def get_activos(self) -> List[Empleado]:
        pass
    
    @abstractmethod
    async def update(self, empleado: Empleado) -> Empleado:
        pass
    
    @abstractmethod
    async def delete(self, empleado_id: str) -> bool:
        pass
    
    @abstractmethod
    async def exists_by_email(self, email: str) -> bool:
        pass
    
    @abstractmethod
    async def exists_by_documento(self, documento: str) -> bool:
        pass