from sqlalchemy.orm import Session
from app.models.ingrediente import Ingrediente
from app.schemas.ingrediente_schema import IngredienteCreate

def get_ingredientes(db: Session):
    return db.query(Ingrediente).all()

def get_ingrediente(db: Session, id_ingrediente: int):
    return db.query(Ingrediente).filter(Ingrediente.id_ingrediente == id_ingrediente).first()

def create_ingrediente(db: Session, ingrediente: IngredienteCreate):
    db_ingrediente = Ingrediente(**ingrediente.dict())
    db.add(db_ingrediente)
    db.commit()
    db.refresh(db_ingrediente)
    return db_ingrediente

def update_ingrediente(db: Session, id_ingrediente: int, ingrediente: IngredienteCreate):
    db_ingrediente = get_ingrediente(db, id_ingrediente)
    if not db_ingrediente:
        return None
    for key, value in ingrediente.dict().items():
        setattr(db_ingrediente, key, value)
    db.commit()
    db.refresh(db_ingrediente)
    return db_ingrediente

def delete_ingrediente(db: Session, id_ingrediente: int):
    db_ingrediente = get_ingrediente(db, id_ingrediente)
    if not db_ingrediente:
        return None
    db.delete(db_ingrediente)
    db.commit()
    return db_ingrediente