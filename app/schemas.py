from typing import Optional
from pydantic import BaseModel, ConfigDict


# ---------- Category ----------
class CategoryBase(BaseModel):
    title: str


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


# ---------- Book ----------
class BookBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: Optional[float] = None
    url: Optional[str] = None
    category_id: int


class BookCreate(BookBase):
    pass


class BookResponse(BookBase):
    id: int
    model_config = ConfigDict(from_attributes=True)