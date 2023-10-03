from fastapi import APIRouter, Depends, HTTPException
from typing import List, Dict  # Import necessary types from the standard typing module
from sqlalchemy.orm import Session
from app.crud.product_crud import get_products, create_product, get_product, update_product
from app.db.database import get_db
from app.db.schemas.products_schema import Product

router = APIRouter()

@router.post("/products/", response_model=Product)
def create_product_route(product: Product, db: Session = Depends(get_db)):
    return create_product(db, product)

@router.get("/products/{product_id}/", response_model=Product)
def read_product_route(product_id: int, db: Session = Depends(get_db)):
    db_product = get_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.put("/products/{product_id}/", response_model=Product)
def update_product_route(product_id: int, product: Product, db: Session = Depends(get_db)):
    db_product = get_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return update_product(db, product_id, product)

@router.get("/products/", response_model=List[Product])
def read_products_route(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_products(db, skip=skip, limit=limit)

