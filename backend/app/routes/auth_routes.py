from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.user_schema import UserCreate, UserRead
from app.services.auth_service import register_user, login_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserRead)
def register_route(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user.nombre, user.email, user.password)

@router.post("/login")
def login_route(user: UserCreate, db: Session = Depends(get_db)):
    return login_user(db, user.email, user.password)
