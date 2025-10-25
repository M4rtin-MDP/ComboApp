from fastapi import HTTPException, status
from passlib.context import CryptContext
from app.repositories.user_repository import get_by_username
from app.core.security import get_password_hash, verify_password, create_access_token
from datetime import timedelta

# === Configuración del contexto bcrypt ===
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# === Funciones de autenticación ===
def authenticate_user(db, username: str, password: str):
    user = get_by_username(db, username)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    return user

def login_user(db, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

def get_password_hash(password: str) -> str:
    """Genera un hash seguro con bcrypt (máx. 72 bytes)"""
    if isinstance(password, bytes):
        password = password.decode("utf-8")
    # Truncamos manualmente si supera los 72 bytes
    password = password[:72]
    return pwd_context.hash(password)

def register_user(db, nombre: str, email: str, password: str):
    existing = get_user_by_email(db, email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed = get_password_hash(password)
    user = create_user(db, nombre, email, hashed)
    return user

   

  


