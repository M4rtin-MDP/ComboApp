from sqlalchemy.orm import Session
import repositories.combo_repository as repo
from schemas import ComboCreate

def listar_combos(db: Session):
    return repo.get_combos(db)

def obtener_combo(db: Session, id_combo: int):
    return repo.get_combo(db, id_combo)

def crear_combo(db: Session, combo: ComboCreate):
    return repo.create_combo(db, combo)

def actualizar_combo(db: Session, id_combo: int, combo: ComboCreate):
    return repo.update_combo(db, id_combo, combo)

def eliminar_combo(db: Session, id_combo: int):
    return repo.delete_combo(db, id_combo)





