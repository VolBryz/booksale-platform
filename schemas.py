# schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional, List


# -----------------------------------------------------
# Book
# -----------------------------------------------------
class BookBase(BaseModel):
    title: str
    author: str
    pages: int
    publisher: str

class BookCreate(BookBase):
    seller_id: Optional[int] = None

class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    pages: Optional[int]
    publisher: Optional[str]

class BookRead(BookBase):
    id: int
    seller_id: Optional[int]

    class Config:
        orm_mode = True


# -----------------------------------------------------
# Seller
# -----------------------------------------------------
class SellerBase(BaseModel):
    first_name: str
    last_name: str
    e_mail: EmailStr

class SellerCreate(SellerBase):
    password: str

class SellerRead(SellerBase):
    id: int
    # Пароль тут отсутствует — нельзя возвращать
    books: List[BookRead] = []

    class Config:
        orm_mode = True

class SellerUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    e_mail: Optional[EmailStr]
    # Пароль не обновляем по заданию

    class Config:
        orm_mode = True
