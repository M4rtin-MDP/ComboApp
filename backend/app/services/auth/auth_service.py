from fastapi import HTTPException, status
from passlib.context import CryptContext
from app.repositories.user_repository import get_by_username
from app.core.security import verify_password, create_access_token


class Auth:
    
    # === Configuración del contexto bcrypt ===
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    # === Funciones de autenticación ===
    @classmethod
    def __authenticate_user(cls, db, username: str, password: str):
        user = get_by_username(db, username)
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )
        return user

    @classmethod
    def login_user(cls, db, username: str, password: str):
        user = cls.__authenticate_user(db, username, password)
        token = create_access_token({"sub": user.username})
        return {"access_token": token, "token_type": "bearer"}


    @classmethod
    def get_password_hash(cls, password: str) -> str:
        """Genera un hash seguro con bcrypt (máx. 72 bytes)"""
        if isinstance(password, bytes):
            password = password.decode("utf-8")
        # Truncamos manualmente si supera los 72 bytes
        password = password[:72]
        return cls.pwd_context.hash(password)

   

  


