from sqlalchemy.orm import Session
from app.repositories.user_repository import get_by_username, create_user
from app.core.security import hash_password

def register_user(db: Session, user):
    existing = get_by_username(db, user.username)
    if existing:
        raise ValueError("Username already exists")
    hashed = hash_password(user.password)
    return create_user(db, user, hashed)
