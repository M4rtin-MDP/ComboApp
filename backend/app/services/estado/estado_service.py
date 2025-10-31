from sqlalchemy.orm import Session
import repositories.estado_repository as repo
from schemas import Estado

def listar_estados(db: Session):
    return repo.get_estados(db)

def obtener_estado(db: Session, id_estado: int):
    return repo.get_estado(db, id_estado)

def crear_estado(db: Session, estado: Estado):
    return repo.create_estado(db, estado)

def actualizar_estado(db: Session, id_estado: int, estado: Estado):
    return repo.update_estado(db, id_estado, estado)

def eliminar_estado(db: Session, id_estado: int):
    return repo.delete_estado(db, id_estado)




