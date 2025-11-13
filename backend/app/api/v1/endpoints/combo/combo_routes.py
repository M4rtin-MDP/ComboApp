from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.combo_schema import Combo, ComboCreate
import app.repositories.combo_repository as repo

router = APIRouter()

@router.get("/", response_model=List[Combo])
def listar_combos(db: Session = Depends(get_db)):
    return repo.get_combos(db)

@router.get("/{id_combo}", response_model=Combo)
def obtener_combo(id_combo: int, db: Session = Depends(get_db)):
    combo = repo.get_combo(db, id_combo)
    if not combo:
        raise HTTPException(status_code=404, detail="Combo no encontrado")
    return combo

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

# ----------------------------------------------------

@router.post("/{id_pedido}", response_model=Combo)
async def crear_combo(id_pedido: int, combo: ComboCreate, db:Session = Depends(get_db)):
        
    #tabla Combo
    create = repo.create_combo(db, combo, id_pedido)
    
    # Enviar los datos para la tabla items_comida e items_ingredientes
    
    if not create:
        raise HTTPException(status_code=404, detail="No se creo el Combo")
    return create

