from pydantic import BaseModel

class ItemComidaBase(BaseModel):
    id_combo: int
    id_comida: int

class ItemComidaCreate(BaseModel):
    id_combo: int
    id_comida: int
    
class ItemComidaResponse(BaseModel):
    item_comida: int
    id_combo: int
    id_comida: int

class ItemComida(ItemComidaBase):

    class Config:
        from_attributes = True
