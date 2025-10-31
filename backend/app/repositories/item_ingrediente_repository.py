from sqlalchemy.orm import Session
from app.models.item_ingrediente import ItemIngrediente
from app.schemas.item_ingrediente_schema import ItemIngredienteCreate

def get_items_ingredientes(db: Session):
    return db.query(ItemIngrediente).all()

def get_item_ingrediente(db: Session, id_item_ingre: int):
    return db.query(ItemIngrediente).filter(ItemIngrediente.id_item_ingre == id_item_ingre).first()

def create_item_ingrediente(db: Session, item: ItemIngredienteCreate):
    db_item = ItemIngrediente(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item_ingrediente(db: Session, id_item_ingre: int, item: ItemIngredienteCreate):
    db_item = get_item_ingrediente(db, id_item_ingre)
    if not db_item:
        return None
    for key, value in item.dict().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item_ingrediente(db: Session, id_item_ingre: int):
    db_item = get_item_ingrediente(db, id_item_ingre)
    if not db_item:
        return None
    db.delete(db_item)
    db.commit()
    return db_item