from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.ingrediente_schema import Ingrediente, IngredienteCreate
import app.repositories.ingrediente_repository as repo

router = APIRouter(prefix="/ingredientes", tags=["Ingredientes"])

@router.get("/", response_model=List[Ingrediente])
def listar_ingredientes(db: Session = Depends(get_db)):
    return repo.get_ingredientes(db)

@router.get("/{id_ingrediente}", response_model=Ingrediente)
def obtener_ingrediente(id_ingrediente: int, db: Session = Depends(get_db)):
    ingrediente = repo.get_ingrediente(db, id_ingrediente)
    if not ingrediente:
        raise HTTPException(status_code=404, detail="Ingrediente no encontrado")
    return ingrediente

@router.post("/", response_model=Ingrediente)
def crear_ingrediente(ingrediente: IngredienteCreate, db: Session = Depends(get_db)):
    return repo.create_ingrediente(db, ingrediente)

@router.put("/{id_ingrediente}", response_model=Ingrediente)
def actualizar_ingrediente(id_ingrediente: int, ingrediente: IngredienteCreate, db: Session = Depends(get_db)):
    updated = repo.update_ingrediente(db, id_ingrediente, ingrediente)
    if not updated:
        raise HTTPException(status_code=404, detail="Ingrediente no encontrado")
    return updated

@router.delete("/{id_ingrediente}", response_model=Ingrediente)
def eliminar_ingrediente(id_ingrediente: int, db: Session = Depends(get_db)):
    deleted = repo.delete_ingrediente(db, id_ingrediente)
    if not deleted:
        raise HTTPException(status_code=404, detail="Ingrediente no encontrado")
    return deleted