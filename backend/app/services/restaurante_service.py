from sqlalchemy.orm import Session
from app.repositories import restaurante_json_repository as repo
from app.schemas.restaurante_schema import  RestauranteDisponible, ComidaSolicitada
from typing import Dict, List


"""Lógica de negocio: matching de combos y cálculo de precios"""
def get_restaurante_json(id_restaurante: int):
    """
    Obtiene el restaurante en formato JSON
    """
    todos_restaurantes = repo.get__todos_restaurantes()
    
    for restaurante in todos_restaurantes:
        if restaurante["id_restaurante"] == id_restaurante:
            return restaurante

def buscar_restaurantes_disponibles(combo: List[ComidaSolicitada]) -> List[Dict]:
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

def puede_preparar_combo(restaurante: Dict, combo: List[ComidaSolicitada]) -> Dict | bool:
    """Verifica si el restaurante tiene la comida con sus ingredientes"""
    
    print(f"Verificando restaurante: {restaurante['nombre']}")
    comidas_combo:List = []
    
    for  comida_solicitada in combo:
        print( comida_solicitada)
        id_comida_solicitada = str(comida_solicitada.id_comida)
        
        # Si no esta disponible, salgo
        if not restaurante["comidas"][id_comida_solicitada]["disponible"]:
            return False
        
        # guardar solamente la comida solicitada
        # diccionario combo + los precios de cada restaurante
        lista_precio_ingr = []
        
        #print(str(comida_solicitada.id_ingrediente))
        # Verifica que tenga todos los ingredientes
        for id_ingrediente in comida_solicitada.id_ingrediente:
            id_ingrediente_solicitada = str(id_ingrediente)

            # Si no esta disponible, salgo
            if not restaurante["ingredientes"][id_ingrediente_solicitada]["disponible"]:
                return False
            
            # TODO: guardar solamente los ingredientes solicitados
            # Guardo el precio del ingrediente
            lista_precio_ingr.append(restaurante["ingredientes"][id_ingrediente_solicitada]["precio"])
            
        
        
        comidas_combo.append({
            'nombre': restaurante["comidas"][id_comida_solicitada]["nombre"],
            'precio_comida': restaurante["comidas"][id_comida_solicitada]["precio"],
            
            'ingredientes': comida_solicitada.ingredientes,
            'precio_ingredientes': lista_precio_ingr
        })

            
    restaurante = {
        'nombre': restaurante["nombre"],
        'latitud': restaurante["latitud"],
        'longitud': restaurante["longitud"],
        'comidas_combo': comidas_combo,  
    }    
    
    return restaurante

