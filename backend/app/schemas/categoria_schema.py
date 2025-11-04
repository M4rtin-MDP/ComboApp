from pydantic import BaseModel

class CategoriaBase(BaseModel):
    id_categoria: int
    nombre: str

class CategoriaCreate(CategoriaBase):
    pass

class Categoria(CategoriaBase):
    class Config:
        from_attributes = True
