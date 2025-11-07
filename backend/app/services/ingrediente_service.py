from sqlalchemy.orm import Session
import repositories.ingrediente_repository as repo
from schemas import IngredienteCreate

def listar_ingredientes(db: Session):
    return repo.get_ingredientes(db)

def obtener_ingrediente(db: Session, id_ingrediente: int):
    return repo.get_ingrediente(db, id_ingrediente)

def crear_ingrediente(db: Session, ingrediente: IngredienteCreate):
    return repo.create_ingrediente(db, ingrediente)

def actualizar_ingrediente(db: Session, id_ingrediente: int, ingrediente: IngredienteCreate):
    return repo.update_ingrediente(db, id_ingrediente, ingrediente)

def eliminar_ingrediente(db: Session, id_ingrediente: int):
    return repo.delete_ingrediente(db, id_ingrediente)





