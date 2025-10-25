from typing import List
from sqlalchemy.orm import Session
from app.models.combo import Combo, combo_ingredient
from app.models.product import Product

def create_combo(db: Session, combo_schema, base, ingredients, bebida, acompanamiento, user_id=None):
    # compute total price
    total = 0.0
    if base: total += base.precio
    for ing in ingredients: total += ing.precio
    if bebida: total += bebida.precio
    if acompanamiento: total += acompanamiento.precio

    db_combo = Combo(nombre=combo_schema.nombre if combo_schema.nombre else None, base=base, bebida=bebida, acompanamiento=acompanamiento, total=total, user_id=user_id)
    db.add(db_combo)
    db.commit()  # commit to get id
    # associate ingredients via insert into association table
    for ing in ingredients:
        db.execute(combo_ingredient.insert().values(combo_id=db_combo.id, product_id=ing.id))
    db.commit()
    db.refresh(db_combo)
    return db_combo

def list_combos(db: Session):
    return db.query(Combo).all()

def get_combo(db: Session, combo_id: int):
    return db.query(Combo).filter(Combo.id == combo_id).first()
