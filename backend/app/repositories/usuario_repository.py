from sqlalchemy.orm import Session
from app.schemas.usuario_schema import UsuarioCreate
from app.models.usuario import Usuario

'''
get, create, update, delete
'''

def get_usuarios(db: Session):
    return db.query(Usuario).all()

def get_usuario(db: Session, usuario_id: str):
    return db.query(Usuario).filter(Usuario.usuario == usuario_id).first()

def get_by_username(db: Session, nombre: str):
    return db.query(Usuario).filter(Usuario.nombre==nombre).first()

def create_usuario(db: Session, usuario: UsuarioCreate):
    db_usuario = usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def update_usuario(db: Session, usuario_id: str, usuario: UsuarioCreate):
    db_usuario = get_usuario(db, usuario_id)
    if not db_usuario:
        return None
    for key, value in usuario.dict().items():
        setattr(db_usuario, key, value)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def delete_usuario(db: Session, usuario_id: str):
    db_usuario = get_usuario(db, usuario_id)
    if not db_usuario:
        return None
    db.delete(db_usuario)
    db.commit()
    return db_usuario