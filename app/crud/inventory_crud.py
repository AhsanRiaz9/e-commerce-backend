from sqlalchemy.orm import Session
from app.db.models import Product, Inventory
from app.db.schemas import inventory_schema, products_schema
from typing import List
from sqlalchemy.orm import Session

from app.crud.product_crud import get_product

def create_inventory(db: Session, inventory_data: inventory_schema.InventoryBase) -> Inventory:
    product_id = inventory_data.get('product_id')
    product = get_product(db, product_id)

    if product:
        inventory = Inventory(**inventory_data)
        db.add(inventory)
        db.commit()
        db.refresh(inventory)
        return inventory
    else:
        return None

def update_inventory_stock(db: Session, inventory_changes_data: inventory_schema.UpdateInventory) -> Inventory:
    product_id = inventory_changes_data.get('product_id')
    addition_quantity = inventory_changes_data.get('addition_quantity')
    product = get_product(db, product_id)

    if product:
        inventory = product.inventory
        if inventory:
            inventory = inventory[0]
            inventory.quantity += addition_quantity
        else:
            inventory = Inventory(product_id=product_id, quantity=addition_quantity)
        db.add(inventory)
        db.commit()
        db.refresh(inventory)
        return inventory
    else:
        return None

def get_inventory(db: Session, inventory_id: int) -> Inventory:
    return db.query(Inventory).get(inventory_id)

def get_all_inventories(db: Session) -> List[Inventory]:
    return db.query(Inventory).all()

def get_low_stocks_inventories(db: Session) -> List[Inventory]:
    return db.query(Inventory).filter(Inventory.quantity==0)


