from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.pedido_schema import Pedido, PedidoCreate
import app.repositories.pedido_repository as repo

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@router.get("/", response_model=List[Pedido])
def listar_pedidos(db: Session = Depends(get_db)):
    return repo.get_pedidos(db)

@router.get("/{id_pedido}", response_model=Pedido)
def obtener_pedido(id_pedido: int, db: Session = Depends(get_db)):
    pedido = repo.get_pedido(db, id_pedido)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido

@router.post("/", response_model=Pedido)
def crear_pedido(pedido: PedidoCreate, db: Session = Depends(get_db)):
    return repo.create_pedido(db, pedido)

@router.put("/{id_pedido}", response_model=Pedido)
def actualizar_pedido(id_pedido: int, pedido: PedidoCreate, db: Session = Depends(get_db)):
    updated = repo.update_pedido(db, id_pedido, pedido)
    if not updated:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return updated

@router.delete("/{id_pedido}", response_model=Pedido)
def eliminar_pedido(id_pedido: int, db: Session = Depends(get_db)):
    deleted = repo.delete_pedido(db, id_pedido)
    if not deleted:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return deleted




