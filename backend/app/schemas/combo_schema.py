from pydantic import BaseModel
from typing import List, Optional

class ComboBase(BaseModel):
    id_pedido: int

class ComboCreate(ComboBase):
    id_pedido: int
    

class Combo(ComboBase):
    id_combo: int

    class Config:
        from_attributes = True
        
class ComboPedidoItem(BaseModel):
    id_pedido: int
    item_comida: int
    comida: str
    ingrediente: Optional[str] = None

    class Config:
        orm_mode = True

    
    
    


