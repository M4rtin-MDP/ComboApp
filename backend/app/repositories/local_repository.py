from sqlalchemy.orm import Session
from app.models.local import Local

def create_local(db: Session, local_data):
    db_local = Local(nombre=local_data.nombre, direccion=local_data.direccion,
                     latitud=local_data.latitud, longitud=local_data.longitud)
    db.add(db_local)
    db.commit()
    db.refresh(db_local)
    return db_local

def add_product_to_local(db: Session, local_id: int, product_id: int):
    lp = LocalProduct(local_id=local_id, product_id=product_id)
    db.add(lp); db.commit(); db.refresh(lp); return lp

def get_locals_by_product_ids(db: Session, product_ids: list):
    # return locals that have any product in product_ids
    q = db.query(Local).join(LocalProduct := LocalProduct.__table__, Local.id==LocalProduct.c.local_id).filter(LocalProduct.c.product_id.in_(product_ids)).all()
    return q

def list_locals(db: Session):
    return db.query(Local).all()

def get_local(db: Session, local_id: int):
    return db.query(Local).filter(Local.id == local_id).first()
