from typing import List
from sqlalchemy.orm import Session
from app.models.estado import Estado

def get_estados(db: Session):
    return db.query(Estado).all()

def get_estado(db: Session, id_estado: int):
    return db.query(Estado).filter(Estado.id_estado == id_estado).first()

def create_estado(db: Session, estado: Estado):
    db_estado = Estado(**estado.dict())
    db.add(db_estado)
    db.commit()
    db.refresh(db_estado)
    return db_estado

def update_estado(db: Session, id_estado: int, estado: Estado):
    db_estado = get_estado(db, id_estado)
    if not db_estado:
        return None
    for key, value in estado.dict().items():
        setattr(db_estado, key, value)
    db.commit()
    db.refresh(db_estado)
    return db_estado

def delete_estado(db: Session, id_estado: int):
    db_estado = get_estado(db, id_estado)
    if not db_estado:
        return None
    db.delete(db_estado)
    db.commit()
    return db_estado