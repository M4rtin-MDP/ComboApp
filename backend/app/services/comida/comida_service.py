from sqlalchemy.orm import Session
import repositories.comida_repository as repo
from schemas import ComidaBaseCreate

def listar_comidas(db: Session):
    return repo.get_comidas(db)

def obtener_comida(db: Session, id_comida: int):
    return repo.get_comida(db, id_comida)

def crear_comida(db: Session, comida: ComidaBaseCreate):
    return repo.create_comida(db, comida)

def actualizar_comida(db: Session, id_comida: int, comida: ComidaBaseCreate):
    return repo.update_comida(db, id_comida, comida)

def eliminar_comida(db: Session, id_comida: int):
    return repo.delete_comida(db, id_comida)





