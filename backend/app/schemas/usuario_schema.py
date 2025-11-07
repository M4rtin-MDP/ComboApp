from pydantic import BaseModel
from typing import Optional

class UsuarioBase(BaseModel):
    mail: str
    direccion: Optional[str] = None
# Para crear un nuevo usuario
class UsuarioCreate(UsuarioBase):
    usuario: str
    contrasena: str

# Para mostrar datos del usuario (por ejemplo, en /auth/me)
class UsuarioRead(UsuarioBase):
    id: Optional[int] = None

class Usuario(UsuarioBase):
    usuario: str
    class Config:
        from_attributes = True
