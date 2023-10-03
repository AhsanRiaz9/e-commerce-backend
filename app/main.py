from fastapi import FastAPI
from app.routers import products_router, inventory_router

app = FastAPI(debug=True)
app.include_router(products_router, prefix="/api", tags=["Products"])
app.include_router(inventory_router, prefix="/api", tags=["Inventory"])

@app.get("/")
def index():
    return {"Hello": "World"}
