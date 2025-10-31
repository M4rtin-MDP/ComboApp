from sqlalchemy.orm import Session
import repositories.restaurante_repository as repo
from schemas import RestauranteCreate

def listar_restaurantes(db: Session):
    return repo.get_restaurantes(db)

def obtener_restaurante(db: Session, id_restaurante: int):
    return repo.get_restaurante(db, id_restaurante)

def crear_restaurante(db: Session, restaurante: RestauranteCreate):
    return repo.create_restaurante(db, restaurante)

def actualizar_restaurante(db: Session, id_restaurante: int, restaurante: RestauranteCreate):
    return repo.update_restaurante(db, id_restaurante, restaurante)

def eliminar_restaurante(db: Session, id_restaurante: int):
    return repo.delete_restaurante(db, id_restaurante)





