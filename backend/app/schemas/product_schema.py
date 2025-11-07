from pydantic import BaseModel
from typing import List, Optional

class ProductBase(BaseModel):
    nombre: str
    tipo: str
    precio: float
    alergenos: Optional[List[str]] = None

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    id: int
    class Config:
        from_attributes = True
