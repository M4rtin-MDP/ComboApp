from pydantic import BaseModel
from typing import List

class ComboBase(BaseModel):
    id_pedido: int

class ComboCreate(ComboBase):
    id_pedido: int
    

class Combo(ComboBase):
    id_combo: int

    class Config:
        from_attributes = True


class ListaCombo(BaseModel):
    comida: str
    ingredientes: List[str]
    
    # Documentacion
    class Config:
        schema_extra = {
            "example": {
                "comida": "hamburguesa",
                "ingredientes": ["manzana", "platano", "naranja", "pera"]
            }
        }