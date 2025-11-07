from pydantic import BaseModel

class IngrComidaBase(BaseModel):
    id: int
    id_comida: int
    id_ingrediente: int

class IngrComidaCreate(IngrComidaBase):
    pass

class IngrComida(IngrComidaBase):

    class Config:
        from_attributes = True
