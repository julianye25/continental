from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from enum import Enum
import uuid


class TipoPago(Enum):
    EFECTIVO = "efectivo"
    TARJETA_CREDITO = "tarjeta_credito"
    TARJETA_DEBITO = "tarjeta_debito"
    TRANSFERENCIA = "transferencia"
    CHEQUE = "cheque"


class EstadoPago(Enum):
    PENDIENTE = "pendiente"
    PROCESANDO = "procesando"
    COMPLETADO = "completado"
    FALLIDO = "fallido"
    REEMBOLSADO = "reembolsado"


@dataclass
class Pago:
    """Entidad Pago"""
    id: Optional[str] = None
    reserva_id: str = ""
    monto: float = 0.0
    tipo_pago: TipoPago = TipoPago.EFECTIVO
    estado: EstadoPago = EstadoPago.PENDIENTE
    fecha_pago: Optional[datetime] = None
    referencia_externa: str = ""  # Para pagos con tarjeta o transferencia
    observaciones: str = ""
    empleado_id: Optional[str] = None  # Quien procesó el pago
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())
        if not self.created_at:
            self.created_at = datetime.now()

    def validate(self) -> list[str]:
        errors = []

        if not self.reserva_id:
            errors.append("El ID de la reserva es obligatorio")

        if self.monto <= 0:
            errors.append("El monto debe ser mayor a 0")

        if (self.tipo_pago in [TipoPago.TARJETA_CREDITO, TipoPago.TARJETA_DEBITO, TipoPago.TRANSFERENCIA]
                and not self.referencia_externa):
            errors.append(
                "La referencia externa es obligatoria para este tipo de pago")

        return errors

    def is_valid(self) -> bool:
        return len(self.validate()) == 0

    def marcar_como_completado(self):
        self.estado = EstadoPago.COMPLETADO
        if not self.fecha_pago:
            self.fecha_pago = datetime.now()
        self.updated_at = datetime.now()

    def esta_completado(self) -> bool:
        return self.estado == EstadoPago.COMPLETADO
