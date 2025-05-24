from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import date, datetime
from ..entities.reserva import Reserva, EstadoReserva

class ReservaRepository(ABC):

    @abstractmethod
    async def create(self, reserva: Reserva) -> Reserva:
        pass

    @abstractmethod
    async def get_by_id(self, reserva_id: str) -> Optional[Reserva]:
        pass

    @abstractmethod
    async def get_all(self, limit: int = 100, offset: int = 0) -> List[Reserva]:
        pass

    @abstractmethod
    async def get_by_cliente(self, cliente_id: str) -> List[Reserva]:
        pass

    @abstractmethod
    async def get_by_habitacion(self, habitacion_id: str) -> List[Reserva]:
        pass

    @abstractmethod
    async def get_by_fechas(self, fecha_inicio: date, fecha_fin: date) -> List[Reserva]:
        pass

    @abstractmethod
    async def get_by_estado(self, estado: EstadoReserva) -> List[Reserva]:
        pass

    @abstractmethod
    async def get_activas(self) -> List[Reserva]:
        pass

    @abstractmethod
    async def check_disponibilidad(self, habitacion_id: str,
                                   fecha_inicio: date, fecha_fin: date) -> bool:
        pass

    @abstractmethod
    async def update(self, reserva: Reserva) -> Reserva:
        pass

    @abstractmethod
    async def delete(self, reserva_id: str) -> bool:
        pass