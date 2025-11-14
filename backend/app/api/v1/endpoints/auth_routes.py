from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.usuario_schema import UsuarioCreate, Login, UsuarioRead
from app.services.auth_service import Auth
from app.services.usuario_service import Usuario

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"] 
)

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    try:
        nuevo_usuario = Usuario.crear_usuario(db, usuario)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
    return Auth.generate_token_for_user(nuevo_usuario)

    
    

@router.post("/login", status_code=status.HTTP_200_OK)
def login(login: Login, db: Session = Depends(get_db)):
    return Auth.login_user(db, login.email, login.password)
