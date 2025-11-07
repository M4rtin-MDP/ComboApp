from pydantic import BaseModel

class ComboBase(BaseModel):
    id_pedido: int

class ComboCreate(ComboBase):
    pass

class Combo(ComboBase):
    id_combo: int

    class Config:
        from_attributes = True
