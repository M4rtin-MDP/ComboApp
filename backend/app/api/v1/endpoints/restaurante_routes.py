from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.restaurante_schema import Restaurante, RestauranteCreate
import app.repositories.restaurante_repository as repo

router = APIRouter(prefix="/restaurantes", tags=["Restaurantes"])

@router.get("/", response_model=List[Restaurante])
def listar_restaurantes(db: Session = Depends(get_db)):
    return repo.get_restaurantes(db)

@router.get("/{id_restaurante}", response_model=Restaurante)
def obtener_restaurante(id_restaurante: int, db: Session = Depends(get_db)):
    restaurante = repo.get_restaurante(db, id_restaurante)
    if not restaurante:
        raise HTTPException(status_code=404, detail="Restaurante no encontrado")
    return restaurante

@router.post("/", response_model=Restaurante)
def crear_restaurante(restaurante: RestauranteCreate, db: Session = Depends(get_db)):
    return repo.create_restaurante(db, restaurante)

@router.put("/{id_restaurante}", response_model=Restaurante)
def actualizar_restaurante(id_restaurante: int, restaurante: RestauranteCreate, db: Session = Depends(get_db)):
    updated = repo.update_restaurante(db, id_restaurante, restaurante)
    if not updated:
        raise HTTPException(status_code=404, detail="Restaurante no encontrado")
    return updated

@router.delete("/{id_restaurante}", response_model=Restaurante)
def eliminar_restaurante(id_restaurante: int, db: Session = Depends(get_db)):
    deleted = repo.delete_restaurante(db, id_restaurante)
    if not deleted:
        raise HTTPException(status_code=404, detail="Restaurante no encontrado")
    return deleted




