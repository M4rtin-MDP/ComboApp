from typing import List
from sqlalchemy.orm import Session
from app.models import ComidaBase
from app.schemas import ComidaBaseCreate
import json

def get_comidas(db: Session):
    return db.query(ComidaBase).all()

def get_comida(db: Session, id_comida: int):
    return db.query(ComidaBase).filter(ComidaBase.id_comida == id_comida).first()

def get_comidas_por_categoria(db: Session, id_categoria: int):
    return db.query(ComidaBase).filter(ComidaBase.id_categoria == id_categoria).all()

def get_clase_producto(db: Session, id_comida: int):
    return db.query(ComidaBase.nombre).filter(ComidaBase.id_comida == id_comida).scalar()



# -------------------------- CHAT ---------------------------------------------------
def create_comida(db: Session, comida: ComidaBaseCreate):
    db_comida = ComidaBase(**comida.dict())
    db.add(db_comida)
    db.commit()
    db.refresh(db_comida)
    return db_comida

def update_comida(db: Session, id_comida: int, comida: ComidaBaseCreate):
    db_comida = get_comida(db, id_comida)
    if not db_comida:
        return None
    for key, value in comida.dict().items():
        setattr(db_comida, key, value)
    db.commit()
    db.refresh(db_comida)
    return db_comida

def delete_comida(db: Session, id_comida: int):
    db_comida = get_comida(db, id_comida)
    if not db_comida:
        return None
    db.delete(db_comida)
    db.commit()
    return db_comida