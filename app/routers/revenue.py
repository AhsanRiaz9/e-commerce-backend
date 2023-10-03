from fastapi import APIRouter, Depends, HTTPException, Query
from app.db.database import get_db
from sqlalchemy.orm import Session
from datetime import date, timedelta
from app.db.models import Sale, Product
from sqlalchemy import func, and_
from typing import List

router = APIRouter()

@router.get("/revenue/daily/{date}", response_model=dict)
def get_daily_revenue(date: date, db: Session = Depends(get_db)):
    next_day = date + timedelta(days=1)

    # Retrieve daily revenue using SQLAlchemy query
    daily_revenue = (
        db.query(func.sum(Product.price * Sale.quantity))
        .join(Sale, Product.id == Sale.product_id)
        .filter(Sale.date >= date, Sale.date < next_day)
        .scalar() or 0.0
    )

    return {'daily_revenue': daily_revenue}


@router.get("/revenue/weekly/{start_date}", response_model=dict)
def get_weekly_revenue(start_date: date, db: Session = Depends(get_db)):
    end_date = start_date + timedelta(days=7)

    weekly_revenue = (
        db.query(func.sum(Product.price * Sale.quantity))
        .join(Sale, Product.id == Sale.product_id)
        .filter(Sale.date >= start_date, Sale.date < end_date)
        .scalar() or 0.0
    )

    return {'weekly_revenue': weekly_revenue}


@router.get("/revenue/annual/{year}", response_model=dict)
def get_annual_revenue(year: int, db: Session = Depends(get_db)):
    start_date = date(year, 1, 1)
    end_date = date(year, 12, 31) + timedelta(days=1)

    annual_revenue = (
        db.query(func.sum(Product.price * Sale.quantity))
        .join(Sale, Product.id == Sale.product_id)
        .filter(Sale.date >= start_date, Sale.date < end_date)
        .scalar() or 0.0
    )

    return {'annual_revenue': annual_revenue}


@router.get("/revenue/compare", response_model=dict)
def compare_revenue(
    start_date: date,
    end_date: date,
    product_ids: List[int] = Query(None),
    categories: List[str] = Query(None),
    db: Session = Depends(get_db)
):
    filters = [Sale.date >= start_date, Sale.date < end_date]

    if product_ids:
        filters.append(Sale.product_id.in_(product_ids))
    if categories:
        filters.append(Product.category.in_(categories))

    filtered_revenue = (
        db.query(Sale.date, func.sum(Product.price * Sale.quantity))
        .join(Product)
        .filter(and_(*filters))
        .group_by(Sale.date)
        .all()
    )

    result = {str(date): float(revenue) for date, revenue in filtered_revenue}
    return result
