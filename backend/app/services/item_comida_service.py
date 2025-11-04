from sqlalchemy.orm import Session
import repositories.item_comida_repository as repo
from schemas import ItemComidaCreate

def listar_items_comida(db: Session):
    return repo.get_items_comida(db)

def obtener_item_comida(db: Session, id_item: int):
    return repo.get_item_comida(db, id_item)

def crear_item_comida(db: Session, item: ItemComidaCreate):
    return repo.create_item_comida(db, item)

def actualizar_item_comida(db: Session, id_item: int, item: ItemComidaCreate):
    return repo.update_item_comida(db, id_item, item)

def eliminar_item_comida(db: Session, id_item: int):
    return repo.delete_item_comida(db, id_item)





