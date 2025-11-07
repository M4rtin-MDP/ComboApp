from pydantic import BaseModel
from typing import Optional

class RestauranteBase(BaseModel):
    nombre: str
    latitud: Optional[float]
    longitud: Optional[float]
    disponible: bool = True

class RestauranteCreate(RestauranteBase):
    pass
class Restaurante(RestauranteBase):
    id_restaurante: int
    class Config:
        from_attributes = True
