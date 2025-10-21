from sqlalchemy.orm import Session
from app.repositories.ingredient_repository import create_ingredient, list_ingredients, get_ingredient

def crear_ingrediente(db: Session, ing):
    return create_ingredient(db, ing)

def listar_ingredientes(db: Session):
    return list_ingredients(db)

def obtener_ingrediente(db: Session, ing_id: int):
    return get_ingredient(db, ing_id)
