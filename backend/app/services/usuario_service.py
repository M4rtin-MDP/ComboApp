from sqlalchemy.orm import Session
from app.repositories import usuario_repository as repo
from app.schemas import UsuarioCreate
from app.core.security import hash_password

class Usuario:
    
    def listar_usuarios(self, db: Session):
        return repo.get_usuarios(db)

    def obtener_usuario(self, db: Session, id_usuario: int):
        return repo.get_usuario(db, id_usuario)

    @staticmethod
    def crear_usuario(db: Session, usuario: UsuarioCreate):
        existente = repo.get_usuario(db, usuario.email)
        if existente:
            raise ValueError("El usuario ya existe.")
        usuario.contrasena = hash_password(usuario.contrasena)
        return repo.create_usuario(db, usuario)

    def actualizar_usuario(self, db: Session, id_usuario: str, usuario: UsuarioCreate):
        existente = repo.get_usuario(db, usuario.nombre)
        if not existente:
            raise ValueError("No se puede actualizar un usuario que no existe")
        usuario.contrasena = hash_password(usuario.contrasena)
        return repo.update_usuario(db, id_usuario, usuario)

    def eliminar_usuario(self, db: Session, id_usuario: str):
        return repo.delete_usuario(db, id_usuario)




