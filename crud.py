# crud.py
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from models import Seller, Book
from schemas import SellerCreate, SellerUpdate, BookCreate, BookUpdate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# --------------
# Seller
# --------------
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_seller(db: Session, seller_data: SellerCreate) -> Seller:
    new_seller = Seller(
        first_name=seller_data.first_name,
        last_name=seller_data.last_name,
        e_mail=seller_data.e_mail,
        password=get_password_hash(seller_data.password),
    )
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller

def get_sellers(db: Session):
    return db.query(Seller).all()

def get_seller_by_id(db: Session, seller_id: int):
    return db.query(Seller).filter(Seller.id == seller_id).first()

def update_seller(db: Session, seller_db: Seller, seller_data: SellerUpdate) -> Seller:
    if seller_data.first_name is not None:
        seller_db.first_name = seller_data.first_name
    if seller_data.last_name is not None:
        seller_db.last_name = seller_data.last_name
    if seller_data.e_mail is not None:
        seller_db.e_mail = seller_data.e_mail
    db.commit()
    db.refresh(seller_db)
    return seller_db

def delete_seller(db: Session, seller_db: Seller):
    db.delete(seller_db)
    db.commit()


# --------------
# Book
# --------------
def create_book(db: Session, book_data: BookCreate) -> Book:
    new_book = Book(
        title=book_data.title,
        author=book_data.author,
        pages=book_data.pages,
        publisher=book_data.publisher,
        seller_id=book_data.seller_id
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def get_books(db: Session):
    return db.query(Book).all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def update_book(db: Session, book_db: Book, book_data: BookUpdate) -> Book:
    if book_data.title is not None:
        book_db.title = book_data.title
    if book_data.author is not None:
        book_db.author = book_data.author
    if book_data.pages is not None:
        book_db.pages = book_data.pages
    if book_data.publisher is not None:
        book_db.publisher = book_data.publisher
    db.commit()
    db.refresh(book_db)
    return book_db

def delete_book(db: Session, book_db: Book):
    db.delete(book_db)
    db.commit()
