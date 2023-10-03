from fastapi import FastAPI
from app.routers import products_router, inventory_router, sales_router, revenue_router
from dotenv import load_dotenv
import os


app = FastAPI(debug=True)


# configure routers with main app
app.include_router(products_router, prefix="/api", tags=["Products"])
app.include_router(inventory_router, prefix="/api", tags=["Inventory"])
app.include_router(sales_router, prefix="/api", tags=["Sales"])
app.include_router(revenue_router, prefix="/api", tags=["Revenue Analytics"])

@app.get("/")
def index():
    return {"Hello": "World"}
