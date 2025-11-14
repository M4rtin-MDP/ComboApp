from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.categoria_schema import Categoria, CategoriaCreate
import app.repositories.categoria_repository as repo

router = APIRouter(
    prefix="/categorias", 
    tags=["Categorias"]
)

@router.get("/", response_model=List[Categoria])
def listar_categorias(db: Session = Depends(get_db)):
    return repo.get_categorias(db)

@router.get("/{id_categoria}", response_model=Categoria)
def obtener_categoria(id_categoria: int, db: Session = Depends(get_db)):
    categoria = repo.get_categoria(db, id_categoria)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria




