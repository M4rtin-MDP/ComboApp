from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Dict
from app.db.database import get_db
from app.schemas.restaurante_schema import Restaurante, ComboRequest, RestauranteDisponible
from app.services import restaurante_service

router = APIRouter(
    prefix="/restaurantes", 
    tags=["Restaurantes"]
)

'''
La data la saca del JSON
'''


'''
    lista_combo: ListaCombo
    
    comida = lista_combo.comida
    ingredientes = lista_combo.ingredientes
    
    # Instancio la clase Producto (Hamburguesa, Pizza, ...) 
    clase_producto:Producto = Registry.create_producto(comida)
    
    for ingrediente in ingredientes:
        # Obtener la clase del ingrediente y decorar el producto
        clase_producto: Producto = Registry.create_ingrediente(ingrediente, clase_producto)
'''

@router.post("/disponibles", response_model=List[Dict])
def listar_restaurantes_disponibles(lista_combo: ComboRequest):
    """
    Busca restaurantes que tengan disponible la comida y sus ingredientes
    """
    return restaurante_service.buscar_restaurantes_disponibles(lista_combo)
# get ubicacion_restaurante



