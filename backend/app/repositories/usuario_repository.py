from sqlalchemy.orm import Session
from app.schemas.usuario_schema import UsuarioCreate
from app.models.usuario import Usuario

'''
get, create, update, delete
'''

def get_usuarios(db: Session):
    return db.query(Usuario).all()

