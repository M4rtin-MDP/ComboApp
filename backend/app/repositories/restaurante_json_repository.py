from sqlalchemy.orm import Session
from app.models import Restaurante
#from schemas.restaurante_schema import ComboRequest, RestauranteDisponible #, ComidaDisponible
import json

'''
Agarra los datos del json
'''

def get_json()-> dict:
    with open('app/repositories/data/datos.json', "r") as f:
        restaurantes:dict = json.load(f)
        
        return restaurantes
    

def get__todos_restaurantes() -> dict:
    return get_json()
    


