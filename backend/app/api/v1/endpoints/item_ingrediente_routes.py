from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.item_ingrediente_schema import ItemIngrediente, ItemIngredienteCreate
import app.repositories.item_ingrediente_repository as repo

router = APIRouter(prefix="/items_ingredientes", tags=["Items_Ingredientes"])

@router.get("/", response_model=List[ItemIngrediente])
def listar_items_ingredientes(db: Session = Depends(get_db)):
    return repo.get_items_ingredientes(db)

@router.get("/{id_item_ingre}", response_model=ItemIngrediente)
def obtener_item_ingrediente(id_item_ingre: int, db: Session = Depends(get_db)):
    item = repo.get_item_ingrediente(db, id_item_ingre)
    if not item:
        raise HTTPException(status_code=404, detail="Item de ingrediente no encontrado")
    return item

@router.post("/", response_model=ItemIngrediente)
def crear_item_ingrediente(item: ItemIngredienteCreate, db: Session = Depends(get_db)):
    return repo.create_item_ingrediente(db, item)

@router.put("/{id_item_ingre}", response_model=ItemIngrediente)
def actualizar_item_ingrediente(id_item_ingre: int, item: ItemIngredienteCreate, db: Session = Depends(get_db)):
    updated = repo.update_item_ingrediente(db, id_item_ingre, item)
    if not updated:
        raise HTTPException(status_code=404, detail="Item de ingrediente no encontrado")
    return updated

@router.delete("/{id_item_ingre}", response_model=ItemIngrediente)
def eliminar_item_ingrediente(id_item_ingre: int, db: Session = Depends(get_db)):
    deleted = repo.delete_item_ingrediente(db, id_item_ingre)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item de ingrediente no encontrado")
    return deleted
