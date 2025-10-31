from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.combo_schema import Combo, ComboCreate
import app.repositories.combo_repository as repo

router = APIRouter(prefix="/combos", tags=["Combos"])

@router.get("/", response_model=List[Combo])
def listar_combos(db: Session = Depends(get_db)):
    return repo.get_combos(db)

@router.get("/{id_combo}", response_model=Combo)
def obtener_combo(id_combo: int, db: Session = Depends(get_db)):
    combo = repo.get_combo(db, id_combo)
    if not combo:
        raise HTTPException(status_code=404, detail="Combo no encontrado")
    return combo

@router.post("/", response_model=Combo)
def crear_combo(combo: ComboCreate, db: Session = Depends(get_db)):
    return repo.create_combo(db, combo)

@router.put("/{id_combo}", response_model=Combo)
def actualizar_combo(id_combo: int, combo: ComboCreate, db: Session = Depends(get_db)):
    updated = repo.update_combo(db, id_combo, combo)
    if not updated:
        raise HTTPException(status_code=404, detail="Combo no encontrado")
    return updated

@router.delete("/{id_combo}", response_model=Combo)
def eliminar_combo(id_combo: int, db: Session = Depends(get_db)):
    deleted = repo.delete_combo(db, id_combo)
    if not deleted:
        raise HTTPException(status_code=404, detail="Combo no encontrado")
    return deleted
