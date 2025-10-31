from typing import List
from sqlalchemy.orm import Session
from app.models.comida import ComidaBase
from app.schemas.comida_base_schema import ComidaBaseCreate
import json

def get_comidas(db: Session):
    return db.query(ComidaBase).all()

def get_comida(db: Session, id_comida: int):
    return db.query(ComidaBase).filter(ComidaBase.id_comida == id_comida).first()

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