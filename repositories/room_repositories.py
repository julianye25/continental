from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import date
from ..domain.entities.Room import Habitacion, TipoHabitacion, EstadoHabitacion

class HabitacionRepository(ABC):
    
    @abstractmethod
    async def create(self, habitacion: Habitacion) -> Habitacion:
        pass
    
    @abstractmethod
    async def get_by_id(self, habitacion_id: str) -> Optional[Habitacion]:
        pass
    
    @abstractmethod
    async def get_by_numero(self, numero: str) -> Optional[Habitacion]:
        pass
    
    @abstractmethod
    async def get_all(self, limit: int = 100, offset: int = 0) -> List[Habitacion]:
        pass
    
    @abstractmethod
    async def get_by_tipo(self, tipo: TipoHabitacion) -> List[Habitacion]:
        pass
    
    @abstractmethod
    async def get_disponibles(self, fecha_inicio: date, fecha_fin: date, 
                             tipo: Optional[TipoHabitacion] = None) -> List[Habitacion]:
        pass
    
    @abstractmethod
    async def update(self, habitacion: Habitacion) -> Habitacion:
        pass
    
    @abstractmethod
    async def delete(self, habitacion_id: str) -> bool:
        pass
    
    @abstractmethod
    async def exists_by_numero(self, numero: str) -> bool:
        pass