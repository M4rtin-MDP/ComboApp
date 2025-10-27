from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserCreate

'''
get, create, update, delete
'''

def create_user(db: Session, user: UserCreate):
    db_user = User(nombre=user.nombre, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_by_username(db: Session, nombre: str):
    return db.query(User).filter(User.nombre == nombre).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()