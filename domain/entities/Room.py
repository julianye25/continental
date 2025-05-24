from enum import Enum
from typing import Optional
from datetime import datetime
from dataclasses import dataclass
import uuid


class TipoHabitacion(Enum):
    SIMPLE = "simple"
    DOBLE = "doble"
    SUITE = "suite"
    PRESIDENTIAL = "presidential"


class EstadoHabitacion(Enum):
    DISPONIBLE = "disponible"
    OCUPADA = "ocupada"
    MANTENIMIENTO = "mantenimiento"
    LIMPIEZA = "limpieza"


@dataclass
class Habitacion:
    """Entidad Habitación"""
    id: Optional[str] = None
    numero: str = ""
    tipo: TipoHabitacion = TipoHabitacion.SIMPLE
    precio_noche: float = 0.0
    capacidad: int = 1
    estado: EstadoHabitacion = EstadoHabitacion.DISPONIBLE
    piso: int = 1
    descripcion: str = ""
    amenities: list[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())
        if not self.created_at:
            self.created_at = datetime.now()
        if self.amenities is None:
            self.amenities = []

    def validate(self) -> list[str]:
        errors = []

        if not self.numero or len(self.numero.strip()) < 1:
            errors.append("El número de habitación es obligatorio")

        if self.precio_noche <= 0:
            errors.append("El precio por noche debe ser mayor a 0")

        if self.capacidad <= 0:
            errors.append("La capacidad debe ser mayor a 0")

        if self.piso <= 0:
            errors.append("El piso debe ser mayor a 0")

        return errors

    def is_valid(self) -> bool:
        return len(self.validate()) == 0

    def esta_disponible(self) -> bool:
        return self.estado == EstadoHabitacion.DISPONIBLE
