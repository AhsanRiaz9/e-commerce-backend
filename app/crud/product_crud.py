from sqlalchemy.orm import Session
from app.db.models import Product
from app.db.schemas import products_schema

def create_product(db: Session, product_data: products_schema.Product):
    product = Product(**product_data.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def update_product(db: Session, product_id: int, product_data: products_schema.Product):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        for key, value in product_data.dict().items():
            setattr(product, key, value)
        db.commit()
        db.refresh(product)
    return product

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip).limit(limit).all()
