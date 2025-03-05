# models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class Seller(Base):
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    e_mail = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    # Продавец может владеть несколькими книгами
    books = relationship("Book", back_populates="seller", cascade="all, delete")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    pages = Column(Integer, nullable=False)
    publisher = Column(String, nullable=False)

    seller_id = Column(Integer, ForeignKey("sellers.id"))
    seller = relationship("Seller", back_populates="books")
