from sqlalchemy.orm import Session
from sqlalchemy import desc 
from app.models import Pedido
from app.schemas import PedidoCreate

def get_pedidos(db: Session):
    return db.query(Pedido).all()

def get_pedido(db: Session, id_pedido: int):
    return db.query(Pedido).filter(Pedido.id_pedido == id_pedido).first()


def get_ultimo_pedido(db: Session, id_usuario: int):
    '''
    Devuevle el ultimo pedido del usuario
    '''
    query = (
        db.query(Pedido)
        .filter(Pedido.id_usuario == id_usuario)
        .order_by(desc(Pedido.id_pedido))
    )
    print("SQL:", query)
    result = query.first()
    print("RESULT:", result)
    return result

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
