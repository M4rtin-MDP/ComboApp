from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List, Dict
from app.db.database import get_db
from app.schemas.restaurante_schema import Restaurante, RestauranteDisponible, ComidaSolicitada
from app.services import restaurante_service
from app.services.precios.precio import PrecioBase
from app.services.precios.decorador import DescuentoCombo, AplicarIVA
import logging


router = APIRouter(
    prefix="/restaurantes", 
    tags=["Restaurantes"]
)

# funciones para ver logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.get("/restaurantes_json/{id_restaurante}", response_model=Dict)
def get_restaurante(id_restaurante: int):
    """
    Busca restaurantes que tengan disponible la comida y sus ingredientes
    """
    return restaurante_service.get_restaurante_json(id_restaurante)


@router.post("/disponibles", response_model=List[Dict])
def listar_restaurantes_disponibles(lista_combo: List[ComidaSolicitada]):
    """
    Busca restaurantes que tengan disponible la comida y sus ingredientes
    """
    return restaurante_service.buscar_restaurantes_disponibles(lista_combo)
# get ubicacion_restaurante


@router.post("/disponibles_total")
def calcular_precio_restaurantes(
    combo: List[ComidaSolicitada]
    ,aplicar_iva: bool = True
) -> List[RestauranteDisponible]:
    
    """
    Calcula precios con diferentes modificadores usando Decorator Pattern
    """
    
    restaurantes_disponibles = restaurante_service.buscar_restaurantes_disponibles(combo)
    resultados = []
        
    try:
        # Calculo los precios del combo para cada restaurante
        for restaurante in restaurantes_disponibles:
            
            # CONSTRUIR EL DECORATOR DINÁMICAMENTE
            calculador = PrecioBase()
            
            # Aplicar descuento combo (siempre si cumple condición)
            #calculador = DescuentoCombo(calculador)
            
            
            # Aplicar IVA
            if aplicar_iva:
                calculador = AplicarIVA(calculador)
            
            # Calcular precio original (sin modificadores)
            precio_original = PrecioBase().calcular_precio(restaurante)
            
            # Calcular precio final (con todos los modificadores)
            precio_final = calculador.calcular_precio(restaurante)
            
            resultados.append(RestauranteDisponible(
                id_restaurante=restaurante["id_restaurante"],
                nombre=restaurante["nombre"],
                latitud= restaurante["latitud"],
                longitud= restaurante["longitud"],
                precio_original=round(precio_original, 2),
                precio_total=round(precio_final, 2),
                #aplicaciones=calculador.obtener_aplicaciones()
            ))
        
            
        
    except Exception as e:
        logger.error(f"Error al procesar los datos: {e}")
        
    return resultados
    
    
    
    


