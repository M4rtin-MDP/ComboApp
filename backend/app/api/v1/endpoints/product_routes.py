from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.product_schema import ProductCreate, ProductRead
from app.repositories.product_repository import create_product, list_products, get_product

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductRead)
def create_product_route(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@router.get("/", response_model=list[ProductRead])
def list_products_route(db: Session = Depends(get_db)):
    return list_products(db)

@router.get("/{product_id}", response_model=ProductRead)
def get_product_route(product_id: int, db: Session = Depends(get_db)):
    p = get_product(db, product_id)
    if not p:
        raise HTTPException(status_code=404, detail="Product not found")
    return p
