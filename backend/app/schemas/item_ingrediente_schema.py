from pydantic import BaseModel

class ItemIngredienteBase(BaseModel):
    id_combo: int
    id_ingrediente: int

class ItemIngredienteCreate(ItemIngredienteBase):
    pass

class ItemIngrediente(ItemIngredienteBase):
    id_item_ingre: int

    class Config:
        from_attributes = True
