from sqlalchemy.orm import Session
import repositories.pedido_repository as repo
from schemas import PedidoCreate

def listar_pedidos(db: Session):
    return repo.get_pedidos(db)

def obtener_pedido(db: Session, id_pedido: int):
    return repo.get_pedido(db, id_pedido)

def crear_pedido(db: Session, pedido: PedidoCreate):
    return repo.create_pedido(db, pedido)

def actualizar_pedido(db: Session, id_pedido: int, pedido: PedidoCreate):
    return repo.update_pedido(db, id_pedido, pedido)

def eliminar_pedido(db: Session, id_pedido: int):
    return repo.delete_pedido(db, id_pedido)




