from pydantic import BaseModel
from typing import List

class ComboBase(BaseModel):
    id_pedido: int

class ComboCreate(ComboBase):
    id_pedido: int
    

class Combo(ComboBase):
    id_combo: int

    class Config:
        from_attributes = True


