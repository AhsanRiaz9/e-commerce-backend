from fastapi import FastAPI
from app.routers import products_router

app = FastAPI(debug=True)
app.include_router(products_router, prefix="/api", tags=["Products"])

@app.get("/")
def index():
    return {"Hello": "World"}
