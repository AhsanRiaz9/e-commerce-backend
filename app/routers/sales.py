from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from typing import List
from app.db.schemas import sales_schema
from app.crud.sales_crud import create_sale, get_sales
from datetime import datetime

router = APIRouter()

@router.post("/sales/", response_model=sales_schema.Sale)
def create_sale_record(sale: sales_schema.SaleCreate, db: Session = Depends(get_db)):
    sale = create_sale(db, sale)
    if sale:
        return sale
    else:
        raise HTTPException(status_code=404, detail="Failure, cannot create sale, either product does not exist or product is out of stock for required quantity.")

@router.get("/sales/", response_model=List[sales_schema.Sale])
def read_sales(
    start_date: datetime = None,
    end_date: datetime = None,
    product_id: int = None,
    category: str = '',
    db: Session = Depends(get_db)
):
    sales = get_sales(db, start_date=start_date, end_date=end_date, product_id=product_id, category=category)
    return sales
