from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field, field_validator


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class ProductCreate(BaseModel):
    name: str = Field(min_length=1)
    current_price: float = Field(gt=0)

    @field_validator("name")
    @classmethod
    def name_must_not_be_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("name cannot be blank")
        return v.strip()


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1)
    current_price: Optional[float] = Field(default=None, gt=0)

    @field_validator("name")
    @classmethod
    def name_must_not_be_blank(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and not v.strip():
            raise ValueError("name cannot be blank")
        return v.strip() if v is not None else v


class ProductOut(BaseModel):
    id: int
    name: str
    current_price: float
    created_at: datetime

    class Config:
        from_attributes = True


class PriceCreate(BaseModel):
    price: float = Field(gt=0)


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
