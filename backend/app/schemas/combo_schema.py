
from pydantic import BaseModel
from typing import List, Optional
from app.schemas.product_schema import ProductRead

class ComboBase(BaseModel):
    nombre: str
    base_meal: str
    # total_price may be computed on server
    precio_total: Optional[float] = 0.0

class ComboCreate(BaseModel):
    nombre: Optional[str] = None
    base_id: int
    ingredient_ids: Optional[List[int]] = []
    bebida_id: Optional[int] = None
    acompanamiento_id: Optional[int] = None
    user_id: Optional[int] = None

class ComboRead(BaseModel):
    id: int
    nombre: Optional[str] = None
    base: Optional[ProductRead] = None
    ingredients: List[ProductRead] = []
    bebida: Optional[ProductRead] = None
    acompanamiento: Optional[ProductRead] = None
    total: float
    user_id: Optional[int] = None

    class Config:
        from_attributes = True
