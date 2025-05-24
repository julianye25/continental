from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import uuid


@dataclass
class ServicioReserva:
    """Entidad que relaciona servicios con reservas"""
    id: Optional[str] = None
    reserva_id: str = ""
    servicio_id: str = ""
    cantidad: int = 1
    precio_unitario: float = 0.0
    precio_total: float = 0.0
    fecha_servicio: Optional[datetime] = None
    observaciones: str = ""
    created_at: Optional[datetime] = None

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())
        if not self.created_at:
            self.created_at = datetime.now()
        if not self.fecha_servicio:
            self.fecha_servicio = datetime.now()

        # Calcular precio total automáticamente
        self.precio_total = self.cantidad * self.precio_unitario

    def validate(self) -> list[str]:
        errors = []

        if not self.reserva_id:
            errors.append("El ID de la reserva es obligatorio")

        if not self.servicio_id:
            errors.append("El ID del servicio es obligatorio")

        if self.cantidad <= 0:
            errors.append("La cantidad debe ser mayor a 0")

        if self.precio_unitario < 0:
            errors.append("El precio unitario no puede ser negativo")

        return errors

    def is_valid(self) -> bool:
        return len(self.validate()) == 0

    def actualizar_precio_total(self):
        """Recalcular el precio total basado en cantidad y precio unitario"""
        self.precio_total = self.cantidad * self.precio_unitario
