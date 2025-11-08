from sqlalchemy.orm import Session
from app.schemas import UsuarioCreate
from app.models import Usuario

'''
get, create, update, delete
'''

def get_usuarios(db: Session):
    return db.query(Usuario).all()

