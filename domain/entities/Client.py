from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import uuid

@dataclass
class Cliente:
    """Entidad Cliente"""
    id: Optional[str] = None
    nombre: str = ""
    apellido: str = ""
    email: str = ""
    telefono: str = ""
    documento: str = ""
    tipo_documento: str = "DNI"
    fecha_nacimiento: Optional[datetime] = None
    nacionalidad: str = ""
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
            errors.append("El nombre debe tener al menos 2 caracteres")
        
        if not self.apellido or len(self.apellido.strip()) < 2:
            errors.append("El apellido debe tener al menos 2 caracteres")
        
        if not self.email or "@" not in self.email:
            errors.append("Email inválido")
        
        if not self.documento or len(self.documento.strip()) < 5:
            errors.append("El documento debe tener al menos 5 caracteres")
        
        return errors
    
    def is_valid(self) -> bool:
        return len(self.validate()) == 0
    
    @property
    def nombre_completo(self) -> str:
        return f"{self.nombre} {self.apellido}"