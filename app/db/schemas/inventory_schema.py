from typing import List
import datetime
from pydantic import BaseModel

class InventoryBase(BaseModel):
    product_id: int
    quantity: int

class Inventory(InventoryBase):
    id: int
    last_updated: datetime.datetime

    class Config:
        orm_mode = True


class UpdateInventory(BaseModel):
    product_id: int
    addition_quantity: int

