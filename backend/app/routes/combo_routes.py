from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.combo_schema import ComboCreate, ComboRead
from app.repositories.combo_repository import create_combo, list_combos, get_combo
from app.repositories.product_repository import get_product

router = APIRouter()

@router.post("/", response_model=ComboRead)
def create_combo_route(combo: ComboCreate, db: Session = Depends(get_db)):
    base = get_product(db, combo.base_id)
    if not base:
        raise HTTPException(status_code=404, detail="Base product not found")
    ingredients = []
    for iid in combo.ingredient_ids or []:
        ing = get_product(db, iid)
        if ing: ingredients.append(ing)
    bebida = get_product(db, combo.bebida_id) if combo.bebida_id else None
    acompanamiento = get_product(db, combo.acompanamiento_id) if combo.acompanamiento_id else None
    db_combo = create_combo(db, combo, base, ingredients, bebida, acompanamiento, user_id=combo.user_id)
    return db_combo

@router.get("/", response_model=list[ComboRead])
def list_combos_route(db: Session = Depends(get_db)):
    return list_combos(db)

@router.get("/{combo_id}", response_model=ComboRead)
def get_combo_route(combo_id: int, db: Session = Depends(get_db)):
    c = get_combo(db, combo_id)
    if not c:
        raise HTTPException(status_code=404, detail="Combo not found")
    return c
