from sqlalchemy.orm import Session
import repositories.categoria_repository as repo
from schemas import CategoriaCreate

def listar_categorias(db: Session):
    return repo.get_categorias(db)

def obtener_categoria(db: Session, id_categoria: int):
    return repo.get_categoria(db, id_categoria)

def crear_categoria(db: Session, categoria: CategoriaCreate):
    return repo.create_categoria(db, categoria)

def actualizar_categoria(db: Session, id_categoria: int, categoria: CategoriaCreate):
    return repo.update_categoria(db, id_categoria, categoria)

def eliminar_categoria(db: Session, id_categoria: int):
    return repo.delete_categoria(db, id_categoria)





