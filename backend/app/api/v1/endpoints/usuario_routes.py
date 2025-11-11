from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.usuario_schema import UsuarioRead, UsuarioCreate
import app.repositories.usuario_repository as repo

router = APIRouter(
    prefix="/usuarios", 
    tags=["Usuarios"]
)

@router.get("/", response_model=List[UsuarioRead])
def listar_usuarios(db: Session = Depends(get_db)):
    return repo.get_usuarios(db)
'''
@router.get("/{id_usuario}", response_model=Usuario)
def obtener_usuario(id_usuario: str, db: Session = Depends(get_db)):
    usuario = repo.get_usuario(db, id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.post("/", response_model=Usuario)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return repo.create_usuario(db, usuario)

@router.put("/{id_usuario}", response_model=Usuario)
def actualizar_usuario(id_usuario: str, usuario: UsuarioCreate, db: Session = Depends(get_db)):
    updated = repo.update_usuario(db, id_usuario, usuario)
    if not updated:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return updated

@router.delete("/{id_usuario}", response_model=Usuario)
def eliminar_usuario(id_usuario: str, db: Session = Depends(get_db)):
    deleted = repo.delete_usuario(db, id_usuario)
    if not deleted:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return deleted

'''


