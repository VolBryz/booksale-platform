# routers/books.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import crud
import schemas
from models import Book
from db import get_db

router = APIRouter(prefix="/api/v1/book", tags=["book"])

@router.post("/", response_model=schemas.BookRead, status_code=status.HTTP_201_CREATED)
def create_book(book_data: schemas.BookCreate, db: Session = Depends(get_db)):
    new_book = crud.create_book(db, book_data)
    return new_book

@router.get("/", response_model=list[schemas.BookRead])
def get_all_books(db: Session = Depends(get_db)):
    books = crud.get_books(db)
    return books

@router.get("/{book_id}", response_model=schemas.BookRead)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    book_db = crud.get_book_by_id(db, book_id)
    if not book_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return book_db

@router.put("/{book_id}", response_model=schemas.BookRead)
def update_book(book_id: int, book_data: schemas.BookUpdate, db: Session = Depends(get_db)):
    book_db = crud.get_book_by_id(db, book_id)
    if not book_db:
        raise HTTPException(status_code=404, detail="Book not found")
    updated_book = crud.update_book(db, book_db, book_data)
    return updated_book

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book_db = crud.get_book_by_id(db, book_id)
    if not book_db:
        raise HTTPException(status_code=404, detail="Book not found")
    crud.delete_book(db, book_db)
    return
