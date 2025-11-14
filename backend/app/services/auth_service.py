from fastapi import HTTPException, status
from passlib.context import CryptContext
from app.repositories import usuario_repository as repo
from app.core import verify_password, create_access_token
from app.schemas.usuario_schema import UsuarioRead, UserResponse, AuthResponse
from typing import Dict


class Auth:
    

    # === Funciones de autenticación ===
    @classmethod
    def __authenticate_user(cls, db, user: str, contrasena_sin_hash: str)-> UsuarioRead:
        usuario = repo.get_usuario(db, user)
        if not usuario or not verify_password(contrasena_sin_hash, usuario.contrasena):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales inválidas"
            )
        return usuario

    @classmethod
    def login_user(cls, db, email: str, contrasena_sin_hash: str):
        usuario: UsuarioRead = cls.__authenticate_user(db, email, contrasena_sin_hash)
        
        return cls.generate_token_for_user(usuario)


    
    @classmethod
    def generate_token_for_user(cls, user: UsuarioRead)-> AuthResponse:
        """Genera un access token para un usuario"""
        token = create_access_token({"sub": user.email})
        
        return AuthResponse(
        access_token=token,
        token_type="bearer",
        user=UserResponse(
            id_usuario=user.id_usuario,
            email=user.email,
            nombre=user.nombre
        )
    )
        