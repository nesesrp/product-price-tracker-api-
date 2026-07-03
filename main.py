from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product Price Tracker API")


@app.get("/")
def root():
    return {"message": "Product Price Tracker API is running"}


@app.post("/products", response_model=schemas.ProductOut)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(name=product.name, current_price=product.current_price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    first_price = models.PriceHistory(product_id=db_product.id, price=db_product.current_price)
    db.add(first_price)
    db.commit()

    return db_product


@app.get("/products", response_model=List[schemas.ProductOut])
def list_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()


@app.get("/products/{product_id}", response_model=schemas.ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.post("/products/{product_id}/price", response_model=schemas.PriceHistoryOut)
def add_price(product_id: int, price: schemas.PriceCreate, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    product.current_price = price.price

    new_price = models.PriceHistory(product_id=product_id, price=price.price)
    db.add(new_price)
    db.commit()
    db.refresh(new_price)

    return new_price


@app.get("/products/{product_id}/price-history", response_model=schemas.PriceHistoryResponse)
def get_price_history(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    history = (
        db.query(models.PriceHistory)
        .filter(models.PriceHistory.product_id == product_id)
        .order_by(models.PriceHistory.recorded_at)
        .all()
    )

    prices = [record.price for record in history]

    return schemas.PriceHistoryResponse(
        product_id=product_id,
        lowest_price=min(prices),
        highest_price=max(prices),
        history=history,
    )


@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    db.query(models.PriceHistory).filter(models.PriceHistory.product_id == product_id).delete()
    db.delete(product)
    db.commit()

    return {"message": "Product deleted"}
