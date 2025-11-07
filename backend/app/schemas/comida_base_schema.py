from pydantic import BaseModel
from typing import Optional

# ----------------------------------------------------
# MODELOS BASE
# ----------------------------------------------------
class ComidaBase(BaseModel):
    id_comida: int
    nombre: str
    categoria_id: Optional[int] = None

# ----------------------------------------------------
# CREACIÓN
# ----------------------------------------------------
class ComidaBaseCreate(ComidaBase):
    """
    Schema para crear una nueva comida base.
    Hereda los campos de ComidaBase y puede extenderse con validaciones.
    """
    pass

# ----------------------------------------------------
# ACTUALIZACIÓN
# ----------------------------------------------------
class ComidaBaseUpdate(BaseModel):
    nombre: Optional[str] = None
    categoria_id: Optional[int] = None

# ----------------------------------------------------
# LECTURA
# ----------------------------------------------------
class ComidaBaseRead(ComidaBase):
    class Config:
        from_attributes = True
