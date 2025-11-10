from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.usuario_schema import UsuarioCreate, UsuarioRead
from app.services.auth_service import Auth
from app.services.usuario_service import Usuario

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"] 
)

@router.post("/register", response_model=UsuarioRead)
def register(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    try:
        return Usuario.crear_usuario(db, usuario)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    # Accepting same payload for simplicity: username + password present
    return Auth.login_user(db, usuario.nombre, usuario.contrasena)

@router.post("/logout")
def logout(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return Auth.logout_user(db, usuario.nombre)     