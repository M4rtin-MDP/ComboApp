from pydantic import BaseModel
from typing import Optional, List
from app.schemas.product_schema import ProductRead

class LocalBase(BaseModel):
    nombre: str
    direccion: Optional[str] = None
    latitud: Optional[float] = None
    longitud: Optional[float] = None

class LocalCreate(LocalBase):
    pass

class LocalRead(LocalBase):
    id: int
    catalogo: Optional[List[ProductRead]] = None
    class Config:
        from_attributes = True
