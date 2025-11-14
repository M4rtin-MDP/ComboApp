from pydantic import BaseModel
from typing import Optional, List, Dict

class RestauranteBase(BaseModel):
    nombre: str
    latitud: Optional[float]
    longitud: Optional[float]
    disponible: bool = True
    productos: List[dict] 
    ingredientes: List[dict]

class RestauranteCreate(RestauranteBase):
    pass
class Restaurante(RestauranteBase):
    id_restaurante: int
    class Config:
        from_attributes = True
        
    
# Se va adevolver una Lista de los restaurante disponibles (para que vea el cliente)
class RestauranteDisponible(BaseModel):
    id_restaurante: int
    nombre: str
    latitud: float
    longitud: float
    #comida_disponible: bool
    precio_original: float
    #ingredientes_disponibles: Dict[str, bool]
    precio_total: float


class ComidaSolicitada(BaseModel):

    id_comida: int
    nombre: str
    id_ingrediente: List[int]
    ingredientes: List[str]
    
    class Config:
        schema_extra = {
            "example": [
                {
                    "id_comida": 1,
                    "nombre": "hamburguesa",
                    "id_ingrediente": [1, 2, 3, 4],
                    "ingredientes": ["manzana", "platano", "naranja", "pera"]
                },
                {
                    "id_comida": 4,
                    "nombre": "agua",
                    "id_ingrediente": [],
                    "ingredientes": []
                },
                {
                    "id_comida": 12,
                    "nombre": "flan",
                    "id_ingrediente": [1],
                    "ingredientes": ["crema"]
                }
            ]
        }


