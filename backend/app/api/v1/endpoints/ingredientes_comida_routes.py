from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.ingr_comida_schema import IngrComida, IngrComidaCreate, IngredientesComida
import app.repositories.ingr_comida_repository as repo

router = APIRouter(
    prefix="/ingredientes_comida", 
    tags=["Ingedientes por Comida"]
)

# Listar los ingredientes segun la comida seleccionada
# //api/v1/ingredientes_comida/{id_comida}
@router.get("/{id_comida}", response_model=List[IngredientesComida])
def listar_ingredientes_comida(id_comida: int, db: Session = Depends(get_db)):
    comida = repo.get_ingredientes_comida(db, id_comida)
    if not comida:
        raise HTTPException(status_code=404, detail="Relación Comida-Ingrediente no encontrada")
    return comida



@router.post("/", response_model=IngrComida)
def crear_ingr_comida(ingr: IngrComidaCreate, db: Session = Depends(get_db)):
    return repo.create_ingr_comida(db, ingr)


@router.delete("/{id_ingr}", response_model=IngrComida)
def eliminar_ingr_comida(id_ingr: int, db: Session = Depends(get_db)):
    deleted = repo.delete_ingr_comida(db, id_ingr)
    if not deleted:
        raise HTTPException(status_code=404, detail="Relación Comida-Ingrediente no encontrada")
    return deleted
