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
    #precio_comida: float
    #ingredientes_disponibles: Dict[str, bool]
    precio_total: float



'''

class ComidaDisponible(BaseModel):
    id_comida: int
    nombre: str
    disponible: bool
    precio: float
    ingredientes_disponibles: Dict[str, bool]
    precio_ingredientes: float
'''

class ComidaSolicitada(BaseModel):
    nombre: str
    id_ingrediente: List[int]
    ingredientes: List[str]


# Lista que recibo del cliente
class ListaCombo(BaseModel):
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
        
        
'''
    {
        "id_comida": 1,
        "comida": "hamburguesa",
        "ingredientes": ["tomate", "lechuga", "carne"]
    },
    {
        "id_comida": 14,
        "comida": "flan",
        "ingredientes": ["crema"]
    }
'''