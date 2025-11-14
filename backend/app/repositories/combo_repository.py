from typing import Optional
from sqlalchemy.orm import Session
from app.models import Combo, ItemComida, ItemIngrediente, ComidaBase, Ingrediente
from app.schemas import ComboCreate

def get_combos(db: Session):
    return db.query(Combo).all()

def get_combo(db: Session, id_combo: int):
    return db.query(Combo).filter(Combo.id_combo == id_combo).first()

def create_combo(db: Session, combo:ComboCreate, id_pedido: Optional[int] = None):
    
    if id_pedido is not None:
        combo.id_pedido = id_pedido
    
    db_combo = Combo(**combo.model_dump())
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

def get_combos_pedido(db: Session, id_pedido: int):
    stmt = (
        db.query(
            Combo.id_pedido,
            ItemComida.item_comida,
            ComidaBase.nombre.label("comida"),
            Ingrediente.nombre.label("ingrediente"),
        )
        .join(ItemComida, ItemComida.id_combo == Combo.id_combo)               # INNER JOIN items_comida
        .outerjoin(ItemIngrediente, ItemIngrediente.item_comida == ItemComida.item_comida)  # LEFT JOIN items_ingredientes
        .join(ComidaBase, ComidaBase.id_comida == ItemComida.id_comida)       # INNER JOIN comida_base
        .outerjoin(Ingrediente, Ingrediente.id_ingrediente == ItemIngrediente.id_ingrediente) # LEFT JOIN ingrediente
        .filter(Combo.id_pedido == id_pedido)
    )

    return stmt.all()