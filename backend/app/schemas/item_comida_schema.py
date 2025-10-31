from pydantic import BaseModel

class ItemComidaBase(BaseModel):
    id_combo: int
    id_comida: int

class ItemComidaCreate(ItemComidaBase):
    pass

class ItemComida(ItemComidaBase):
    id: int

    class Config:
        from_attributes = True
