from typing import List
from sqlalchemy.orm import Session
from app.models.ingredient_model import Ingredient
from app.schemas.ingredient_schema import IngredientCreate

def create_ingredient(db: Session, ing: IngredientCreate):
    db_ing = Ingredient(name=ing.name, price=ing.price)
    db.add(db_ing)
    db.commit()
    db.refresh(db_ing)
    return db_ing

def list_ingredients(db: Session) -> List[Ingredient]:
    return db.query(Ingredient).all()

def get_ingredient(db: Session, ing_id: int):
    return db.query(Ingredient).filter(Ingredient.id == ing_id).first()
