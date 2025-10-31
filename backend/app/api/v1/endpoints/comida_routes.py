from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.comida_base_schema import ComidaBase, ComidaBaseCreate
import app.repositories.comida_repository as repo

router = APIRouter(prefix="/comidas", tags=["Comidas"])

@router.get("/", response_model=List[ComidaBase])
def listar_comidas(db: Session = Depends(get_db)):
    return repo.get_comidas(db)

@router.get("/{id_comida}", response_model=ComidaBase)
def obtener_comida(id_comida: int, db: Session = Depends(get_db)):
    comida = repo.get_comida(db, id_comida)
    if not comida:
        raise HTTPException(status_code=404, detail="Comida no encontrada")
    return comida

@router.post("/", response_model=ComidaBase)
def crear_comida(comida: ComidaBaseCreate, db: Session = Depends(get_db)):
    return repo.create_comida(db, comida)

@router.put("/{id_comida}", response_model=ComidaBase)
def actualizar_comida(id_comida: int, comida: ComidaBaseCreate, db: Session = Depends(get_db)):
    updated = repo.update_comida(db, id_comida, comida)
    if not updated:
        raise HTTPException(status_code=404, detail="Comida no encontrada")
    return updated

@router.delete("/{id_comida}", response_model=ComidaBase)
def eliminar_comida(id_comida: int, db: Session = Depends(get_db)):
    deleted = repo.delete_comida(db, id_comida)
    if not deleted:
        raise HTTPException(status_code=404, detail="Comida no encontrada")
    return deleted



