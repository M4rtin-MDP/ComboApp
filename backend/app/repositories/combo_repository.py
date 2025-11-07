from typing import List
from sqlalchemy.orm import Session
from app.models.combo import Combo
from app.schemas.combo_schema import ComboCreate

def get_combos(db: Session):
    return db.query(Combo).all()

def get_combo(db: Session, id_combo: int):
    return db.query(Combo).filter(Combo.id_combo == id_combo).first()

def create_combo(db: Session, combo: ComboCreate):
    db_combo = Combo(**combo.dict())
    db.add(db_combo)
    db.commit()
    db.refresh(db_combo)
    return db_combo

def update_combo(db: Session, id_combo: int, combo: ComboCreate):
    db_combo = get_combo(db, id_combo)
    if not db_combo:
        return None
    for key, value in combo.dict().items():
        setattr(db_combo, key, value)
    db.commit()
    db.refresh(db_combo)
    return db_combo

def delete_combo(db: Session, id_combo: int):
    db_combo = get_combo(db, id_combo)
    if not db_combo:
        return None
    db.delete(db_combo)
    db.commit()
    return db_combo