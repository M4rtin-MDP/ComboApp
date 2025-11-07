from sqlalchemy.orm import Session
from app.models.pedido import Pedido
from app.schemas.pedido_schema import PedidoCreate

def get_pedidos(db: Session):
    return db.query(Pedido).all()

def get_pedido(db: Session, id_pedido: int):
    return db.query(Pedido).filter(Pedido.id_pedido == id_pedido).first()

def create_pedido(db: Session, pedido: PedidoCreate):
    db_pedido = Pedido(**pedido.dict())
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido

def update_pedido(db: Session, id_pedido: int, pedido: PedidoCreate):
    db_pedido = get_pedido(db, id_pedido)
    if not db_pedido:
        return None
    for key, value in pedido.dict().items():
        setattr(db_pedido, key, value)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido

def delete_pedido(db: Session, id_pedido: int):
    db_pedido = get_pedido(db, id_pedido)
    if not db_pedido:
        return None
    db.delete(db_pedido)
    db.commit()
    return db_pedido
