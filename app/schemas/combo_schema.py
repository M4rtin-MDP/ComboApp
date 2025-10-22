from pydantic import BaseModel
from typing import List, Optional

class ComboBase(BaseModel):
    name: str
    base_meal: str
    # total_price may be computed on server
    total_price: Optional[float] = 0.0

class ComboCreate(ComboBase):
    ingredient_ids: List[int] = []  # IDs of ingredients

class ComboRead(ComboBase):
    id: int
    user_id: int
    ingredients: List[dict] = []
    class Config:
        from_attributes = True
