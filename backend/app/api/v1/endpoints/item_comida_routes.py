from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.item_comida_schema import ItemComida, ItemComidaCreate
import app.repositories.item_comida_repository as repo

router = APIRouter(prefix="/items_comida", tags=["Items_Comida"])

@router.get("/", response_model=List[ItemComida])
def listar_items_comida(db: Session = Depends(get_db)):
    return repo.get_items_comida(db)

@router.get("/{id_item}", response_model=ItemComida)
def obtener_item_comida(id_item: int, db: Session = Depends(get_db)):
    item = repo.get_item_comida(db, id_item)
    if not item:
        raise HTTPException(status_code=404, detail="Item de comida no encontrado")
    return item

@router.post("/", response_model=ItemComida)
def crear_item_comida(item: ItemComidaCreate, db: Session = Depends(get_db)):
    return repo.create_item_comida(db, item)

@router.put("/{id_item}", response_model=ItemComida)
def actualizar_item_comida(id_item: int, item: ItemComidaCreate, db: Session = Depends(get_db)):
    updated = repo.update_item_comida(db, id_item, item)
    if not updated:
        raise HTTPException(status_code=404, detail="Item de comida no encontrado")
    return updated

@router.delete("/{id_item}", response_model=ItemComida)
def eliminar_item_comida(id_item: int, db: Session = Depends(get_db)):
    deleted = repo.delete_item_comida(db, id_item)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item de comida no encontrado")
    return deleted
