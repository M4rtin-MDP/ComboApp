from typing import List
from sqlalchemy.orm import Session
from app.models.ingr_comida import IngrComida
from app.schemas.ingr_comida_schema import IngrComidaCreate


def get_ingredientes_comida(db: Session, comida: int):
    return db.query(IngrComida).filter(IngrComida.id_comida == comida).all()

def create_ingr_comida(db: Session, ingr: IngrComidaCreate):
    db_ingr = IngrComida(**ingr.dict())
    db.add(db_ingr)
    db.commit()
    db.refresh(db_ingr)
    return db_ingr



def delete_ingr_comida(db: Session, id_ingr: int):
    db_ingr = get_ingredientes_comida(db, id_ingr)
    if not db_ingr:
        return None
    db.delete(db_ingr)
    db.commit()
    return db_ingr