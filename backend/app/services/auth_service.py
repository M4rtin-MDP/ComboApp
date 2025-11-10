from fastapi import HTTPException, status
from passlib.context import CryptContext
from app.repositories import usuario_repository as repo
from app.core import verify_password, create_access_token


class Auth:
    
    # === Configuración del contexto bcrypt ===
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    # === Funciones de autenticación ===
    @classmethod
    def __authenticate_user(cls, db, nombre: str, contrasena_sin_hash: str):
        usuario = repo.get_usuario(db, nombre)
        if not usuario or not verify_password(contrasena_sin_hash, usuario.contrasena):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )
        return usuario

    @classmethod
    def login_user(cls, db, nombre: str, contrasena_sin_hash: str):
        usuario = cls.__authenticate_user(db, nombre, contrasena_sin_hash)
        token = create_access_token({"sub": usuario.nombre})
        return {"access_token": token, "token_type": "bearer"}


    @classmethod
    def get_password_hash(cls, password: str) -> str:
        """Genera un hash seguro con bcrypt (máx. 72 bytes)"""
        if isinstance(password, bytes):
            password = password.decode("utf-8")
        # Truncamos manualmente si supera los 72 bytes
        password = password[:72]
        return cls.pwd_context.hash(password)