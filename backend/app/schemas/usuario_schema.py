from pydantic import BaseModel
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: str
    direccion: Optional[str] = None
    
class Login(BaseModel):
    email: str
    password: str
    
# Para crear un nuevo usuario
class UsuarioCreate(UsuarioBase):
    email: str
    contrasena: str
    

# Para mostrar datos del usuario (por ejemplo, en /auth/me)
class UsuarioRead(UsuarioBase):
    id_usuario: int
    email: str
    class Config:
        from_attributes = True
        
        
# Modelo de respuesta
class UserResponse(BaseModel):
    id_usuario: int
    email: str
    nombre: str

class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse
