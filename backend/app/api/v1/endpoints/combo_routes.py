from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.combo_schema import ComboCreate, ComboRead
from app.services.combo_service import crear_combo, listar_combos, obtener_combo

router = APIRouter()

@router.post("/", response_model=ComboRead)
def crear(combo: ComboCreate, db: Session = Depends(get_db)):
    # For MVP, require client to send user_id in payload; in future tie to JWT current user
    return crear_combo(db, combo, combo_schema_user_id(combo))

def combo_schema_user_id(combo):
    # simple helper: if user_id present in payload, use it; else 0
    try:
        return int(getattr(combo, "user_id", 0))
    except:
        return 0

@router.get("/", response_model=list[ComboRead])
def listar(db: Session = Depends(get_db)):
    return listar_combos(db)

@router.get("/{combo_id}", response_model=ComboRead)
def obtener(combo_id: int, db: Session = Depends(get_db)):
    item = obtener_combo(db, combo_id)
    if not item:
        raise HTTPException(status_code=404, detail="Combo not found")
    return item
