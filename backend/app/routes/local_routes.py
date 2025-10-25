from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.local_schema import LocalCreate, LocalRead
from app.repositories.local_repository import create_local, list_locals, get_local

router = APIRouter(prefix="/locals", tags=["Locals"])

@router.post("/", response_model=LocalRead)
def create_local_route(local: LocalCreate, db: Session = Depends(get_db)):
    return create_local(db, local)

@router.get("/", response_model=list[LocalRead])
def list_locals_route(db: Session = Depends(get_db)):
    return list_locals(db)

@router.get("/{local_id}", response_model=LocalRead)
def get_local_route(local_id: int, db: Session = Depends(get_db)):
    l = get_local(db, local_id)
    if not l:
        raise HTTPException(status_code=404, detail="Local not found")
    return l

@router.post("/{local_id}/products/{product_id}")
def add_product_route(local_id: int, product_id: int, db: Session = Depends(get_db)):
    return add_product_to_local(db, local_id, product_id)

@router.get("/search", response_model=list[LocalRead])
def search_locals(product_ids: list[int] = Query(...), db: Session = Depends(get_db)):
    return get_locals_by_product_ids(db, product_ids)
