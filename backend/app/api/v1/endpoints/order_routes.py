from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.repositories.order_repository import create_order, list_orders
from app.schemas.order_schema import OrderCreate, OrderRead


router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/", response_model=OrderRead)
def create_order_route(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db, order)

@router.get("/", response_model=list[OrderRead])
def list_orders_route(db: Session = Depends(get_db)):
    return list_orders(db)
