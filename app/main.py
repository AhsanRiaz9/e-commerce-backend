from fastapi import FastAPI
from app.routers import products_router, inventory_router, sales_router

app = FastAPI(debug=True)

# configure routers with main app
app.include_router(products_router, prefix="/api", tags=["Products"])
app.include_router(inventory_router, prefix="/api", tags=["Inventory"])
app.include_router(sales_router, prefix="/api", tags=["Sales"])


@app.get("/")
def index():
    return {"Hello": "World"}
