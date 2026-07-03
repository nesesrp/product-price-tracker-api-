from datetime import datetime
from typing import List

from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    current_price: float


class ProductOut(BaseModel):
    id: int
    name: str
    current_price: float
    created_at: datetime

    class Config:
        from_attributes = True


class PriceCreate(BaseModel):
    price: float


class PriceHistoryOut(BaseModel):
    id: int
    price: float
    recorded_at: datetime

    class Config:
        from_attributes = True


class PriceHistoryResponse(BaseModel):
    product_id: int
    lowest_price: float
    highest_price: float
    history: List[PriceHistoryOut]
