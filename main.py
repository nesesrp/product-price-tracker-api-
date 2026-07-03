from fastapi import FastAPI

from database import products_db
from models import Product

app = FastAPI(title="Product Price Tracker API")


@app.get("/")
def root():
    return {"message": "Product Price Tracker API is running"}


@app.post("/products", response_model=Product)
def create_product(product: Product):
    product.id = len(products_db) + 1
    products_db.append(product)
    return product
