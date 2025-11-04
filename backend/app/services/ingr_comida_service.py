from sqlalchemy.orm import Session
import repositories.ingr_comida_repository as repo
from schemas import IngrComidaCreate

def listar_ingr_comidas(db: Session):
    return repo.get_ingr_comidas(db)

def obtener_ingr_comida(db: Session, id_ingr: int):
    return repo.get_ingr_comida(db, id_ingr)

def crear_ingr_comida(db: Session, ingr: IngrComidaCreate):
    return repo.create_ingr_comida(db, ingr)

def actualizar_ingr_comida(db: Session, id_ingr: int, ingr: IngrComidaCreate):
    return repo.update_ingr_comida(db, id_ingr, ingr)

def eliminar_ingr_comida(db: Session, id_ingr: int):
    return repo.delete_ingr_comida(db, id_ingr)




