from sqlalchemy.orm import Session
from app.models import Restaurante
from app.schemas import ListaCombo, RestauranteDisponible #, ComidaDisponible
import json


def get_json() -> dict:
    with open('app/repositories/data/datos.json', "r") as f:
        restaurantes:dict = json.load(f)
        
        return restaurantes

def get_restaurante(db: Session, id_restaurante: int):
    return db.query(Restaurante).filter(Restaurante.id_restaurante == id_restaurante).first()



def listar_restaurantes_disponibles(combo: ListaCombo):
    datos = get_json()

    resultados = []
    
    for restaurante in datos:
        precio_total_restaurante = 0.0
        todo_disponible = True
        
        # Verificar cada comida solicitada
        for id_comida, comida_solicitada in combo.comidas.items():
            id_comida_solicitada = str(id_comida)
            
            
            comidas_restaurante = restaurante["comidas"][id_comida_solicitada]
            
            # Veo si esta disponible la comida
            if not comidas_restaurante["disponible"]:
                todo_disponible = False
                break
            
            print('existe la comida')
            
            # Verificar ingredientes de esta comida
            precio_ingredientes = 0.0
            ingredientes_disponibles = True
            
            for id_ingrediente in comida_solicitada.id_ingrediente:
                id_ingr_solicitado = str(id_ingrediente)
                
                if id_ingr_solicitado in restaurante["ingredientes"]:
                    
                    ing_data = restaurante["ingredientes"][id_ingr_solicitado]
                    
                    if ing_data["disponible"]:
                        precio_ingredientes += ing_data["precio"]
                    else:

                        ingredientes_disponibles = False
                        break
                else:
                    # El restaurante no tiene este ingrediente
                    ingredientes_disponibles = False
                    break
            
            # Si algún ingrediente no está disponible, esta comida no cumple
            if not ingredientes_disponibles:
                todo_disponible = False
                break
            
            # Agregar esta comida al resultado
            '''comidas_disponibles.append(ComidaDisponible(
                id_comida=int(id_comida),
                nombre=comida_rest["nombre"],
                disponible=True,
                precio=comida_rest["precio"],
                ingredientes_disponibles=ingredientes_estado,
                precio_ingredientes=precio_ingredientes
            ))'''
            
            precio_total_restaurante += comidas_restaurante["precio"] + precio_ingredientes

        
        # Si todas las comidas están OK, agregar el restaurante
        if todo_disponible:
            resultados.append(RestauranteDisponible(
                #id=restaurante["id"],
                nombre=restaurante["nombre"],
                latitud=restaurante["latitud"],
                longitud=restaurante["longitud"],
                #comidas=comidas_disponibles,
                precio_total=precio_total_restaurante,
                #todas_disponibles=True
            ))
            
    print(resultados)
    
    return resultados


'''
def buscar_restaurantes_disponibles(combo: ListaCombo):
    """
    Busca restaurantes que tengan disponible la comida y sus ingredientes
    """
    resultados = []
    
    for restaurante in RESTAURANTES_DB:
        # Verificar si el restaurante tiene la comida solicitada
        comida_key = str(combo.id_comida)
        
        if comida_key not in restaurante["comidas"]:
            continue
            
        comida = restaurante["comidas"][comida_key]
        
        # Verificar disponibilidad de la comida
        if not comida["disponible"]:
            continue
        
        # Verificar disponibilidad de ingredientes
        ingredientes_estado = {}
        precio_ingredientes = 0.0
        todos_disponibles = True
        
        for ingrediente in combo.ingredientes:
            if ingrediente in restaurante["ingredientes"]:
                ing_data = restaurante["ingredientes"][ingrediente]
                ingredientes_estado[ingrediente] = ing_data["disponible"]
                
                if ing_data["disponible"]:
                    precio_ingredientes += ing_data["precio"]
                else:
                    todos_disponibles = False
            else:
                ingredientes_estado[ingrediente] = False
                todos_disponibles = False
        
        # Solo agregar si todos los ingredientes están disponibles
        if todos_disponibles:
            resultados.append(RestauranteDisponible(
                id=restaurante["id"],
                nombre=restaurante["nombre"],
                latitud=restaurante["latitud"],
                longitud=restaurante["longitud"],
                comida_disponible=True,
                precio_comida=comida["precio"],
                ingredientes_disponibles=ingredientes_estado,
                precio_total=comida["precio"] + precio_ingredientes
            ))
    
    return resultados
    

'''