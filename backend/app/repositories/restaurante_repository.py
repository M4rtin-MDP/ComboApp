from sqlalchemy.orm import Session
from app.models import Restaurante
from app.schemas.restaurante_schema import ComboRequest, RestauranteDisponible #, ComidaDisponible


'''
Modifica la tabla Restaurantes 
'''

def get_restaurante(db: Session, id_restaurante: int):
    return db.query(Restaurante).filter(Restaurante.id_restaurante == id_restaurante).first()

