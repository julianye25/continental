from dataclasses import dataclass
from datetime import datetime, date
from typing import Optional
from enum import Enum
import uuid

class TipoEmpleado(Enum):
    RECEPCIONISTA = "recepcionista"
    GERENTE = "gerente"
    LIMPIEZA = "limpieza"
    MANTENIMIENTO = "mantenimiento"
    SEGURIDAD = "seguridad"
    ADMINISTRADOR = "administrador"

class EstadoEmpleado(Enum):
    ACTIVO = "activo"
    INACTIVO = "inactivo"
    VACACIONES = "vacaciones"
    LICENCIA = "licencia"

@dataclass
class Empleado:
    """Entidad Empleado"""
    id: Optional[str] = None
    nombre: str = ""
    apellido: str = ""
    email: str = ""
    telefono: str = ""
    documento: str = ""
    tipo: TipoEmpleado = TipoEmpleado.RECEPCIONISTA
    estado: EstadoEmpleado = EstadoEmpleado.ACTIVO
    salario: float = 0.0
    fecha_ingreso: Optional[date] = None
    turno: str = ""  # "mañana", "tarde", "noche"
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    def _post_init_(self):
        if not self.id:
            self.id = str(uuid.uuid4())
        if not self.created_at:
            self.created_at = datetime.now()
        if not self.fecha_ingreso:
            self.fecha_ingreso = date.today()
    
    def validate(self) -> list[str]:
        errors = []
        
        if not self.nombre or len(self.nombre.strip()) < 2:
            errors.append("El nombre debe tener al menos 2 caracteres")
        
        if not self.apellido or len(self.apellido.strip()) < 2:
            errors.append("El apellido debe tener al menos 2 caracteres")
        
        if not self.email or "@" not in self.email:
            errors.append("Email inválido")
        
        if not self.documento or len(self.documento.strip()) < 5:
            errors.append("El documento debe tener al menos 5 caracteres")
        
        if self.salario < 0:
            errors.append("El salario no puede ser negativo")
        
        if self.turno and self.turno not in ["mañana", "tarde", "noche"]:
            errors.append("El turno debe ser: mañana, tarde o noche")
        
        return errors
    
    def is_valid(self) -> bool:
        return len(self.validate()) == 0
    
    @property
    def nombre_completo(self) -> str:
        return f"{self.nombre} {self.apellido}"
    
    def esta_activo(self) -> bool:
        return self.estado == EstadoEmpleado.ACTIVO