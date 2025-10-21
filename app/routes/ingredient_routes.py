from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.ingredient_schema import IngredientCreate, IngredientRead
from app.services.ingredient_service import crear_ingrediente, listar_ingredientes, obtener_ingrediente

router = APIRouter(prefix="/ingredients", tags=["Ingredients"])

@router.post("/", response_model=IngredientRead)
def crear(ing: IngredientCreate, db: Session = Depends(get_db)):
    return crear_ingrediente(db, ing)

@router.get("/", response_model=list[IngredientRead])
def listar(db: Session = Depends(get_db)):
    return listar_ingredientes(db)

@router.get("/{ing_id}", response_model=IngredientRead)
def obtener(ing_id: int, db: Session = Depends(get_db)):
    item = obtener_ingrediente(db, ing_id)
    if not item:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return item
