from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from enum import Enum
import uuid

class TipoServicio(Enum):
    RESTAURANTE = "restaurante"
    SPA = "spa"
    LAVANDERIA = "lavanderia"
    TRANSPORTE = "transporte"
    WIFI = "wifi"
    DESAYUNO = "desayuno"
    GIMNASIO = "gimnasio"
    PISCINA = "piscina"
    OTRO = "otro"

class EstadoServicio(Enum):
    ACTIVO = "activo"
    INACTIVO = "inactivo"
    MANTENIMIENTO = "mantenimiento"

@dataclass
class Servicio:
    """Entidad Servicio"""
    id: Optional[str] = None
    nombre: str = ""
    descripcion: str = ""
    tipo: TipoServicio = TipoServicio.OTRO
    precio: float = 0.0
    estado: EstadoServicio = EstadoServicio.ACTIVO
    incluido_en_tarifa: bool = False
    horario_inicio: str = ""  # "08:00"
    horario_fin: str = ""     # "22:00"
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    def _post_init_(self):
        if not self.id:
            self.id = str(uuid.uuid4())
        if not self.created_at:
            self.created_at = datetime.now()
    
    def validate(self) -> list[str]:
        errors = []
        
        if not self.nombre or len(self.nombre.strip()) < 2:
            errors.append("El nombre del servicio debe tener al menos 2 caracteres")
        
        if self.precio < 0:
            errors.append("El precio no puede ser negativo")
        
        if not self.incluido_en_tarifa and self.precio == 0:
            errors.append("Si el servicio no está incluido en la tarifa, debe tener un precio")
        
        return errors
    
    def is_valid(self) -> bool:
        return len(self.validate()) == 0
    
    def esta_disponible(self) -> bool:
        return self.estado == EstadoServicio.ACTIVO
    
    def es_gratuito(self) -> bool:
        return self.precio == 0 or self.incluido_en_tarifa