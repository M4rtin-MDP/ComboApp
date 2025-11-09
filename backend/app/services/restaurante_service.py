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

        if puede_preparar_combo(restaurante, combo):
            restaurantes_disponibles.append(restaurante)
            
    return restaurantes_disponibles

def puede_preparar_combo(restaurante: Dict, combo: ComboRequest) -> bool:
    """Verifica si el restaurante tiene la comida con sus ingredientes"""
    for id_comida, comida_solicitada in combo.comidas.items():
        id_comida_solicitada = str(id_comida)
        
        # Verifica que tenga la comida base
        if id_comida_solicitada not in restaurante["comidas"]:
            return False
        # TODO: guardar solamente la comida solicitada
        
        
        # Verifica que tenga todos los ingredientes
        for id_ingrediente in comida_solicitada.id_ingrediente:
            id_ingrediente_solicitada = str(id_ingrediente)
            if id_ingrediente_solicitada not in restaurante["ingredientes"]:
                return False
            
            # TODO: guardar solamente los ingredientes solicitados
    
    return True

