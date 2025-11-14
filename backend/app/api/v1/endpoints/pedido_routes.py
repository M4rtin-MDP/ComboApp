from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.pedido_schema import Pedido, PedidoCreate
from app.repositories import pedido_repository as repo
from app.api.v1.endpoints.combo.combo_routes import crear_combo

router = APIRouter(
    prefix="/pedidos", 
    tags=["Pedidos"]
)


@router.get("/", response_model=List[Pedido])
def listar_pedidos(db: Session = Depends(get_db)):
    return repo.get_pedidos(db)

@router.get("/id/{id_pedido}", response_model=Pedido)
def obtener_pedido(id_pedido: int, db: Session = Depends(get_db)):
    pedido = repo.get_pedido(db, id_pedido)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido


@router.get("/usuario/{id_usuario}", response_model=List[Pedido])
def obtener_pedidos_usuario(id_usuario: int, db: Session = Depends(get_db)):
    pedido = repo.get_pedidos_usuario(db, id_usuario)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido

@router.post("/", response_model=Pedido)
def crear_pedido(pedido: PedidoCreate, db: Session = Depends(get_db)):

    '''
    Al confirmar el pedido, se crea los fatos de la tabla pedido
    '''
    create_pedido = repo.create_pedido(db, pedido)
    
    return create_pedido

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




