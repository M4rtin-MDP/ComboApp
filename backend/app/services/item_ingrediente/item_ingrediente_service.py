from sqlalchemy.orm import Session
import repositories.item_ingrediente_repository as repo
from schemas import ItemIngredienteCreate

def listar_items_ingredientes(db: Session):
    return repo.get_items_ingredientes(db)

def obtener_item_ingrediente(db: Session, id_item_ingre: int):
    return repo.get_item_ingrediente(db, id_item_ingre)

def crear_item_ingrediente(db: Session, item: ItemIngredienteCreate):
    return repo.create_item_ingrediente(db, item)

def actualizar_item_ingrediente(db: Session, id_item_ingre: int, item: ItemIngredienteCreate):
    return repo.update_item_ingrediente(db, id_item_ingre, item)

def eliminar_item_ingrediente(db: Session, id_item_ingre: int):
    return repo.delete_item_ingrediente(db, id_item_ingre)





