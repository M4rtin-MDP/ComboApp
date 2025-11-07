from sqlalchemy.orm import Session
from app.models.restaurante import Restaurante
from app.schemas.restaurante_schema import RestauranteCreate

def get_restaurantes(db: Session):
    return db.query(Restaurante).all()

def get_restaurante(db: Session, id_restaurante: int):
    return db.query(Restaurante).filter(Restaurante.id_restaurante == id_restaurante).first()

def create_restaurante(db: Session, restaurante: RestauranteCreate):
    db_restaurante = Restaurante(**restaurante.dict())
    db.add(db_restaurante)
    db.commit()
    db.refresh(db_restaurante)
    return db_restaurante

def update_restaurante(db: Session, id_restaurante: int, restaurante: RestauranteCreate):
    db_restaurante = get_restaurante(db, id_restaurante)
    if not db_restaurante:
        return None
    for key, value in restaurante.dict().items():
        setattr(db_restaurante, key, value)
    db.commit()
    db.refresh(db_restaurante)
    return db_restaurante

def delete_restaurante(db: Session, id_restaurante: int):
    db_restaurante = get_restaurante(db, id_restaurante)
    if not db_restaurante:
        return None
    db.delete(db_restaurante)
    db.commit()
    return db_restaurante