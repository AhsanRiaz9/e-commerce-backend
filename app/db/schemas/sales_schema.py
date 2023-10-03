from pydantic import BaseModel, conint
from datetime import datetime

class SaleCreate(BaseModel):
    product_id: int
    quantity: conint(ge=1)  # ge=1 means greater than or equal to 1

class SaleBase(SaleCreate):
    date: datetime


class Sale(SaleBase):
    id: int


    class Config:
        orm_mode = True
