from fastapi import APIRouter, Depends, HTTPException
from app.db.schemas import inventory_schema
from typing import List
from app.crud import inventory_crud
from sqlalchemy.orm import Session
from app.db.database import get_db
router = APIRouter()

@router.get("/inventory/", response_model=List[inventory_schema.Inventory])
def read_all_inventories(db: Session = Depends(get_db)):
    inventories = inventory_crud.get_all_inventories(db)
    return inventories

@router.get("/inventory/low_stock/", response_model=List[inventory_schema.Inventory])
def read_low_stock_inventories(db: Session = Depends(get_db)):
    inventories = inventory_crud.get_low_stocks_inventories(db)
    return inventories

@router.get("/inventory/{inventory_id}/", response_model=inventory_schema.Inventory)
def read_inventory(inventory_id: int, db: Session = Depends(get_db)):
    inventory = inventory_crud.get_inventory(db, inventory_id)
    if inventory:
        return inventory
    else:
        raise HTTPException(status_code=404, detail="Inventory not found")

@router.post("/inventory/", response_model=inventory_schema.InventoryBase)
def create_inventory(inventory_data: inventory_schema.InventoryBase, db: Session = Depends(get_db)):
    inventory = inventory_crud.create_inventory(db, inventory_data.dict())
    if inventory:
        return inventory
    else:
        raise HTTPException(status_code=404, detail=f"Product not found. You need to first create a product then assign inventory.")

@router.put("/inventory/update_stock/", response_model=inventory_schema.Inventory)
def update_inventory_stock(inventory_changes_data: inventory_schema.UpdateInventory, db: Session = Depends(get_db)):
    inventory = inventory_crud.update_inventory_stock(db, inventory_changes_data.dict())
    if inventory:
        return inventory
    else:
        raise HTTPException(status_code=404, detail=f"Product not found. You need to first create a product then update the stock.")
