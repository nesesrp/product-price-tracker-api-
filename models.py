from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    id: Optional[int] = None
    name: str
    url: str
    current_price: float
    target_price: float
