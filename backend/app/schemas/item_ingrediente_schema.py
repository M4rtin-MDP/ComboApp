from pydantic import BaseModel

class ItemIngredienteBase(BaseModel):
    item_comida: int
    id_ingrediente: int

class ItemIngredienteCreate(BaseModel):
    item_comida: int
    id_ingrediente: int

class ItemIngrediente(ItemIngredienteBase):
    item_ingrediente: int

    class Config:
        from_attributes = True
