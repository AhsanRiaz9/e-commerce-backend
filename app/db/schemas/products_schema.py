from typing import List
from pydantic import BaseModel, confloat
from datetime import datetime

class ProductBase(BaseModel):
    name: str
    category: str
    price: confloat(ge=1)


class Product(ProductBase):
    id: int
    class Config:
        orm_mode = True

class ProductWithSales(Product):
    sales: List['Sale'] = []

class ProductWithInventory(Product):
    inventory: List['Inventory'] = []
