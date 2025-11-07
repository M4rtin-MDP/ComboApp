from typing import List
from sqlalchemy.orm import Session
from app.models.item_comida import ItemComida
from app.schemas.item_comida_schema import ItemComidaCreate

def get_items_comida(db: Session):
    return db.query(ItemComida).all()

def get_item_comida(db: Session, id_item: int):
    return db.query(ItemComida).filter(ItemComida.id == id_item).first()

def create_item_comida(db: Session, item: ItemComidaCreate):
    db_item = ItemComida(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item_comida(db: Session, id_item: int, item: ItemComidaCreate):
    db_item = get_item_comida(db, id_item)
    if not db_item:
        return None
    for key, value in item.dict().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item_comida(db: Session, id_item: int):
    db_item = get_item_comida(db, id_item)
    if not db_item:
        return None
    db.delete(db_item)
    db.commit()
    return db_item