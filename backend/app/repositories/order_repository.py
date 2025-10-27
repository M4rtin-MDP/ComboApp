from sqlalchemy.orm import Session
from app.models.order import Order

def create_order(db: Session, order_create):
    db_order = Order(combo_id=order_create.combo_id, user_id=order_create.user_id,
                     local_id=order_create.local_id, estado="pendiente", total=None)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def list_orders(db: Session):
    return db.query(Order).all()
