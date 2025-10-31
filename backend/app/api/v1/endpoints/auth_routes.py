from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.usuario_schema import UsuarioCreate, UsuarioRead
from app.services.auth.auth_service import Auth

router = APIRouter()

@router.post("/register", response_model=UsuarioRead)
def register(user: UsuarioCreate, db: Session = Depends(get_db)):
    try:
        return Usuario.register_user(db, usuario)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(user: UsuarioCreate, db: Session = Depends(get_db)):
    # Accepting same payload for simplicity: username + password present
    return Auth.login_user(db, usuario.nombre, usuario.password)

@router.post("/logout")
def logout(user: UsuarioCreate, db: Session = Depends(get_db)):
    return Auth.logout_user(db, usuario.nombre)     