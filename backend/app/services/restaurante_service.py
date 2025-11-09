from sqlalchemy.orm import Session
from app.repositories import restaurante_json_repository as repo
from app.schemas.restaurante_schema import  ComboRequest, RestauranteDisponible
from typing import Dict, List


"""Lógica de negocio: matching de combos y cálculo de precios"""


def buscar_restaurantes_disponibles(combo: ComboRequest) -> List[Dict]:
    """
    Filtra restaurantes que tienen TODOS los items del combo.
    """
    todos_restaurantes = repo.get__todos_restaurantes() # se puede pensar algun filtro para que no agarre todos los restaurantes
    restaurantes_disponibles = []
    
    for restaurante in todos_restaurantes:

        restaurante_combo = puede_preparar_combo(restaurante, combo)
        
        if restaurante_combo:
            restaurantes_disponibles.append(restaurante_combo)
            
    return restaurantes_disponibles

def puede_preparar_combo(restaurante: Dict, combo: ComboRequest) -> Dict | bool:
    """Verifica si el restaurante tiene la comida con sus ingredientes"""
     
    comidas_combo:dict = {}
    
    for id_comida, comida_solicitada in combo.comidas.items():
        id_comida_solicitada = str(id_comida)
        
        # Si no esta disponible, salgo
        if not restaurante["comidas"][id_comida_solicitada]["disponible"]:
            return False
        
        # guardar solamente la comida solicitada
        # diccionario combo + los precios de cada restaurante
        lista_precio_ingr = []
        
        # Verifica que tenga todos los ingredientes
        for id_ingrediente in comida_solicitada.id_ingrediente:
            id_ingrediente_solicitada = str(id_ingrediente)

            # Si no esta disponible, salgo
            if not restaurante["ingredientes"][id_ingrediente_solicitada]["disponible"]:
                return False
            
            # TODO: guardar solamente los ingredientes solicitados
            # Guardo el precio del ingrediente
            lista_precio_ingr.append(restaurante["ingredientes"][id_ingrediente_solicitada]["precio"])
            
        
        comidas_combo[id_comida_solicitada] = {
            'nombre': restaurante["comidas"][id_comida_solicitada]["nombre"],
            'precio_comida': restaurante["comidas"][id_comida_solicitada]["precio"],
            
            'ingredientes': comida_solicitada.ingredientes,
            'precio_ingredientes': lista_precio_ingr
        }
            
    restaurante = {
        'nombre': restaurante["nombre"],
        'latitud': restaurante["latitud"],
        'longitud': restaurante["longitud"],
        'comidas_combo': comidas_combo,  
    }    
    
    return restaurante

def agregar_precio(combo: ComboRequest, comida_restaurante, ingredientes_restaurante):
    
    
    
    pass