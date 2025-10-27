from typing import List
from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product_schema import ProductCreate
import json

def create_product(db: Session, product: ProductCreate):
    al = None
    if product.alergenos:
        al = json.dumps(product.alergenos)
    db_product = Product(nombre=product.nombre, tipo=product.tipo, precio=product.precio, alergenos=al)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def list_products(db: Session) -> List[Product]:
    return db.query(Product).all()

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()
