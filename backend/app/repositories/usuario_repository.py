from sqlalchemy.orm import Session
from app.schemas import UsuarioCreate
from app.models import Usuario


def get_usuarios(db: Session):
    return db.query(Usuario).all()

def get_usuario(db: Session, user_email: str):
    return db.query(Usuario).filter(Usuario.email == user_email).first()

def get_usuario_id(db: Session, user_email: str):
    '''
        Obtiene el ID del usuario a partir de su email
    '''
    return db.query(Usuario.id_usuario).filter(Usuario.email == user_email).first()

def create_usuario(db: Session, usuario: UsuarioCreate):
    db_usuario = Usuario(**usuario.model_dump())
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
