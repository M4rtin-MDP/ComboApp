from sqlalchemy.orm import Session
import app.repositories.usuario_repository as repo
from app.schemas.usuario_schema import UsuarioCreate

def listar_usuarios(db: Session):
    return repo.get_usuarios(db)

def obtener_usuario(db: Session, usuario_id: str):
    return repo.get_usuario(db, usuario_id)

def crear_usuario(db: Session, usuario: UsuarioCreate):
    # Ejemplo de validación
    existente = repo.get_usuario(db, usuario.usuario)
    if existente:
        raise ValueError("El usuario ya existe.")
    return repo.create_usuario(db, usuario)

def actualizar_usuario(db: Session, usuario_id: str, usuario: UsuarioCreate):
    return repo.update_usuario(db, usuario_id, usuario)

def eliminar_usuario(db: Session, usuario_id: str):
    return repo.delete_usuario(db, usuario_id)




