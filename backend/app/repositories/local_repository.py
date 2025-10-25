from sqlalchemy.orm import Session
from app.models.local import Local

def create_local(db: Session, local_data):
    db_local = Local(nombre=local_data.nombre, direccion=local_data.direccion,
                     latitud=local_data.latitud, longitud=local_data.longitud)
    db.add(db_local)
    db.commit()
    db.refresh(db_local)
    return db_local

def list_locals(db: Session):
    return db.query(Local).all()

def get_local(db: Session, local_id: int):
    return db.query(Local).filter(Local.id == local_id).first()
