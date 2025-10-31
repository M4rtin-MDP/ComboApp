from pydantic import BaseModel

class IngrComidaBase(BaseModel):
    id_comida: int
    id_ingrediente: int

class IngrComidaCreate(IngrComidaBase):
    pass

class IngrComida(IngrComidaBase):
    id: int

    class Config:
        from_attributes = True
