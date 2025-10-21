from pydantic import BaseModel
from typing import Optional

class IngredientBase(BaseModel):
    name: str
    price: float

class IngredientCreate(IngredientBase):
    pass

class IngredientRead(IngredientBase):
    id: int
    class Config:
        from_attributes = True
