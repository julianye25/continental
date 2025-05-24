from dataclasses import dataclass
from datetime import datetime, date
from typing import Optional, List
from enum import Enum
import uuid

class EstadoReserva(Enum):
    PENDIENTE = "pendiente"
    CONFIRMADA = "confirmada"
    CHECK_IN = "check_in"
    CHECK_OUT = "check_out"
    CANCELADA = "cancelada"
    NO_SHOW = "no_show"

@dataclass
class Reserva:
    """Entidad Reserva"""
    id: Optional[str] = None
    cliente_id: str = ""
    habitacion_id: str = ""
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    fecha_check_in: Optional[datetime] = None
    fecha_check_out: Optional[datetime] = None
    huespedes: int = 1
    precio_total: float = 0.0
    estado: EstadoReserva = EstadoReserva.PENDIENTE
    observaciones: str = ""
    servicios_adicionales: List[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())
        if not self.created_at:
            self.created_at = datetime.now()
        if self.servicios_adicionales is None:
            self.servicios_adicionales = []

    def validate(self) -> list[str]:
        errors = []

        if not self.cliente_id:
            errors.append("El ID del cliente es obligatorio")

        if not self.habitacion_id:
            errors.append("El ID de la habitación es obligatorio")

        if not self.fecha_inicio:
            errors.append("La fecha de inicio es obligatoria")

        if not self.fecha_fin:
            errors.append("La fecha de fin es obligatoria")

        if self.fecha_inicio and self.fecha_fin:
            if self.fecha_inicio >= self.fecha_fin:
                errors.append("La fecha de inicio debe ser anterior a la fecha de fin")

            if self.fecha_inicio < date.today():
                errors.append("La fecha de inicio no puede ser en el pasado")

        if self.huespedes <= 0:
            errors.append("El número de huéspedes debe ser mayor a 0")

        if self.precio_total < 0:
            errors.append("El precio total no puede ser negativo")

        return errors

    def is_valid(self) -> bool:
        return len(self.validate()) == 0

    def calcular_noches(self) -> int:
        if self.fecha_inicio and self.fecha_fin:
            return (self.fecha_fin - self.fecha_inicio).days
        return 0

    def puede_hacer_check_in(self) -> bool:
        return (self.estado == EstadoReserva.CONFIRMADA and
                self.fecha_inicio <= date.today())

    def puede_hacer_check_out(self) -> bool:
        return self.estado == EstadoReserva.CHECK_IN