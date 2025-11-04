from pydantic import BaseModel

class IngredienteBase(BaseModel):
    id_ingrediente: int
    nombre: str


class IngredienteCreate(IngredienteBase):
    pass

class Ingrediente(IngredienteBase):
    class Config:
        from_attributes = True
