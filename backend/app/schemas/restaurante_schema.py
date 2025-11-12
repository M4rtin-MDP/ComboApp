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
    nombre: str
    latitud: float
    longitud: float
    #comida_disponible: bool
    precio_original: float
    #ingredientes_disponibles: Dict[str, bool]
    precio_total: float


class ComidaSolicitada(BaseModel):
    nombre: str
    id_ingrediente: List[int]
    ingredientes: List[str]
    
    class Config:
        schema_extra = {
                1: {
                    "nombre": "hamburguesa",
                    "id_ingrediente":[1, 2, 3, 4],
                    "ingredientes": ["manzana", "platano", "naranja", "pera"]
                },
                
                4:{
                    "nombre": "agua",
                    "id_ingrediente": [],
                    "ingredientes": []
                },
                
                12:{
                    "comida": "flan", 
                    "id_ingrediente":[1],
                    "ingredientes": ["crema"]
                }
        }


# Lista que recibo del cliente
class ComboRequest(BaseModel):
    comidas: Dict[int, ComidaSolicitada]
    
    # Documentacion
    class Config:
        schema_extra = {
            "example":{
                1: {
                    "nombre": "hamburguesa",
                    "id_ingrediente":[1, 2, 3, 4],
                    "ingredientes": ["manzana", "platano", "naranja", "pera"]
                },
                
                4:{
                    "nombre": "agua",
                    "id_ingrediente": [],
                    "ingredientes": []
                },
                
                12:{
                    "comida": "flan", 
                    "id_ingrediente":[1],
                    "ingredientes": ["crema"]
                }
            }
        }
        