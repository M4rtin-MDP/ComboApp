from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.ingr_comida_schema import IngrComida, IngrComidaCreate
import app.repositories.ingr_comida_repository as repo

router = APIRouter(prefix="/ingr_comidas", tags=["Ingr_Comidas"])

@router.get("/", response_model=List[IngrComida])
def listar_ingr_comidas(db: Session = Depends(get_db)):
    return repo.get_ingr_comidas(db)

@router.get("/{id_ingr}", response_model=IngrComida)
def obtener_ingr_comida(id_ingr: int, db: Session = Depends(get_db)):
    ingr = repo.get_ingr_comida(db, id_ingr)
    if not ingr:
        raise HTTPException(status_code=404, detail="Relación Comida-Ingrediente no encontrada")
    return ingr

@router.post("/", response_model=IngrComida)
def crear_ingr_comida(ingr: IngrComidaCreate, db: Session = Depends(get_db)):
    return repo.create_ingr_comida(db, ingr)

@router.put("/{id_ingr}", response_model=IngrComida)
def actualizar_ingr_comida(id_ingr: int, ingr: IngrComidaCreate, db: Session = Depends(get_db)):
    updated = repo.update_ingr_comida(db, id_ingr, ingr)
    if not updated:
        raise HTTPException(status_code=404, detail="Relación Comida-Ingrediente no encontrada")
    return updated

@router.delete("/{id_ingr}", response_model=IngrComida)
def eliminar_ingr_comida(id_ingr: int, db: Session = Depends(get_db)):
    deleted = repo.delete_ingr_comida(db, id_ingr)
    if not deleted:
        raise HTTPException(status_code=404, detail="Relación Comida-Ingrediente no encontrada")
    return deleted
