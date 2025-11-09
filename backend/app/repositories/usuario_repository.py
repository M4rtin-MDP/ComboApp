from sqlalchemy.orm import Session
from app.schemas import UsuarioCreate
from app.models import Usuario


def get_usuarios(db: Session):
    return db.query(Usuario).all()

def get_usuario(db: Session, id_usuario: int):
    return db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()

def get_usuario(db: Session, nombre: str):
    return db.query(Usuario).filter(Usuario.nombre == nombre).first()

def create_usuario(db: Session, usuario: Usuario):
    db_usuario = Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def update_usuario(db: Session, id_usuario: int, usuario: Usuario):
    db_usuario = get_usuario(db, id_usuario)
    if not db_usuario:
        return None
    for key, value in usuario.dict().items():
        setattr(db_usuario, key, value)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def delete_usuario(db: Session, id_usuario: int):
    db_usuario = get_usuario(db, id_usuario)
    if not db_usuario:
        return None
    db.delete(db_usuario)
    db.commit()
    return db_usuario
