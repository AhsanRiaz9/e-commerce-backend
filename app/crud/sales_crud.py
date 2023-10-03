from datetime import datetime
from typing import List

from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.crud.product_crud import get_product
from app.db.models import Sale, Product
from app.db.schemas import sales_schema


def create_sale(db: Session, sale: sales_schema.SaleCreate):
    product = get_product(db, sale.product_id)
    if product and product.inventory and product.inventory.quantity >= sale.quantity:
        db_sale = Sale(**sale.dict())
        db.add(db_sale)
        db.commit()
        db.refresh(db_sale)

        # Update inventory
        product.inventory.quantity -= sale.quantity
        db.commit()

        return db_sale
    else:
        return None


def get_sales(db: Session, start_date: datetime = None, end_date: datetime = None, product_id: int = None,
              category: str = '') -> List[Sale]:
    filters = []

    if start_date:
        filters.append(Sale.date >= start_date)

    if end_date:
        filters.append(Sale.date <= end_date)

    if product_id:
        filters.append(Sale.product_id == product_id)

    if category:
        filters.append(Product.category == category)

    # Construct the final filter condition
    filter_condition = and_(*filters)

    # Execute the query with the filter condition
    filtered_sales = db.query(Sale).join(Product).filter(filter_condition).all()

    return filtered_sales
