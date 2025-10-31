from typing import List
from sqlalchemy.orm import Session
from app.models.categoria import Categoria
from app.schemas.categoria_schema import CategoriaCreate

def get_categorias(db: Session):
    return db.query(Categoria).all()

def get_categoria(db: Session, id_categoria: int):
    return db.query(Categoria).filter(Categoria.id_categoria == id_categoria).first()

def create_categoria(db: Session, categoria: CategoriaCreate):
    db_categoria = Categoria(**categoria.dict())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def update_categoria(db: Session, id_categoria: int, categoria: CategoriaCreate):
    db_categoria = get_categoria(db, id_categoria)
    if not db_categoria:
        return None
    for key, value in categoria.dict().items():
        setattr(db_categoria, key, value)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def delete_categoria(db: Session, id_categoria: int):
    db_categoria = get_categoria(db, id_categoria)
    if not db_categoria:
        return None
    db.delete(db_categoria)
    db.commit()
    return db_categoria