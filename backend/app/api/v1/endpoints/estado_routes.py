from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas import Estado
from  app.repositories import estado_repository as repo

router = APIRouter(
    prefix="/estados", 
    tags=["Estados"]
)

@router.get("/", response_model=List[Estado])
def listar_estados(db: Session = Depends(get_db)):
    return repo.get_estados(db)

@router.get("/{id_estado}", response_model=Estado)
def obtener_estado(id_estado: int, db: Session = Depends(get_db)):
    estado = repo.get_estado(db, id_estado)
    if not estado:
        raise HTTPException(status_code=404, detail="Estado no encontrado")
    return estado


@router.put("/{id_estado}", response_model=Estado)
def actualizar_estado(id_estado: int, estado: Estado, db: Session = Depends(get_db)):
    updated = repo.update_estado(db, id_estado, estado)
    if not updated:
        raise HTTPException(status_code=404, detail="Estado no encontrado")
    return updated

