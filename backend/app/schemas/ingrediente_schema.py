from pydantic import BaseModel

class IngredienteBase(BaseModel):
    nombre: str
    disponible: bool
    precio: float

class IngredienteCreate(IngredienteBase):
    pass

class Ingrediente(IngredienteBase):
    id_ingrediente: int
    class Config:
        from_attributes = True
