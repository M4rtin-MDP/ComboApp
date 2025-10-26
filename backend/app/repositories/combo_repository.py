from sqlalchemy.orm import Session
from app.models.combo import Combo
from app.schemas.combo_schema import ComboCreate

def create_combo(db: Session, combo: ComboCreate, user_id: int, ingredients):
    db_combo = Combo(name=combo.name, base_meal=combo.base_meal, user_id=user_id)
    
    
    total = 0.0
    for ing in ingredients:
        total += ing.price
    db_combo.total_price = total
    db_combo.ingredients = ingredients
    db.add(db_combo)
    db.commit()
    db.refresh(db_combo)
    return db_combo

def list_combos(db: Session):
    return db.query(Combo).all()

def get_combo(db: Session, combo_id: int):
    return db.query(Combo).filter(Combo.id == combo_id).first()
