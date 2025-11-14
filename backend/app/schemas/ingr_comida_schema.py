from pydantic import BaseModel

class IngrComidaBase(BaseModel):
    id_comida: int
    id_ingrediente: int

class IngrComidaCreate(IngrComidaBase):
    pass

class IngrComida(IngrComidaBase):
    nombre: str
    class Config:
        from_attributes = True


class IngredientesComida(BaseModel):
    id_ingrediente: int
    nombre: str

    class Config:
        from_attributes = True