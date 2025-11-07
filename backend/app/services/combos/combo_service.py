from sqlalchemy.orm import Session
from app.repositories.combo_repository import create_combo, list_combos, get_combo
from app.repositories.ingredient_repository import get_ingredient

def crear_combo(db: Session, combo_schema, user_id: int):
    # fetch ingredient objects
    ingredients = [get_ingredient(db, iid) for iid in combo_schema.ingredient_ids]
    ingredients = [i for i in ingredients if i is not None]
    return create_combo(db, combo_schema, user_id, ingredients)

def listar_combos(db: Session):
    return list_combos(db)

def obtener_combo(db: Session, combo_id: int):
    return get_combo(db, combo_id)
