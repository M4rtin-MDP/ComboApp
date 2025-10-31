from typing import List
from sqlalchemy.orm import Session
from app.models.ingr_comida import IngrComida
from app.schemas.ingr_comida_schema import IngrComidaCreate

def get_ingr_comidas(db: Session):
    return db.query(IngrComida).all()

def get_ingr_comida(db: Session, id_ingr: int):
    return db.query(IngrComida).filter(IngrComida.id == id_ingr).first()

def create_ingr_comida(db: Session, ingr: IngrComidaCreate):
    db_ingr = IngrComida(**ingr.dict())
    db.add(db_ingr)
    db.commit()
    db.refresh(db_ingr)
    return db_ingr

def update_ingr_comida(db: Session, id_ingr: int, ingr: IngrComidaCreate):
    db_ingr = get_ingr_comida(db, id_ingr)
    if not db_ingr:
        return None
    for key, value in ingr.dict().items():
        setattr(db_ingr, key, value)
    db.commit()
    db.refresh(db_ingr)
    return db_ingr

def delete_ingr_comida(db: Session, id_ingr: int):
    db_ingr = get_ingr_comida(db, id_ingr)
    if not db_ingr:
        return None
    db.delete(db_ingr)
    db.commit()
    return db_ingr