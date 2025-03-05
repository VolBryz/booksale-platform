# routers/sellers.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db import get_db
import crud
import schemas
from models import Seller

router = APIRouter(prefix="/api/v1/seller", tags=["seller"])


@router.post("/", response_model=schemas.SellerRead, status_code=status.HTTP_201_CREATED)
def create_seller(seller_data: schemas.SellerCreate, db: Session = Depends(get_db)):
    # Проверяем, что нет другого продавца с таким e_mail
    existing = db.query(Seller).filter(Seller.e_mail == seller_data.e_mail).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Seller with this e_mail already exists."
        )
    new_seller = crud.create_seller(db, seller_data)
    return new_seller


@router.get("/", response_model=list[schemas.SellerRead])
def get_all_sellers(db: Session = Depends(get_db)):
    sellers = crud.get_sellers(db)
    return sellers


@router.get("/{seller_id}", response_model=schemas.SellerRead)
def get_seller_by_id(seller_id: int, db: Session = Depends(get_db)):
    seller_db = crud.get_seller_by_id(db, seller_id)
    if not seller_db:
        raise HTTPException(status_code=404, detail="Seller not found")
    return seller_db


@router.put("/{seller_id}", response_model=schemas.SellerRead)
def update_seller(
    seller_id: int,
    seller_data: schemas.SellerUpdate,
    db: Session = Depends(get_db)
):
    seller_db = crud.get_seller_by_id(db, seller_id)
    if not seller_db:
        raise HTTPException(status_code=404, detail="Seller not found")
    updated = crud.update_seller(db, seller_db, seller_data)
    return updated


@router.delete("/{seller_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_seller(seller_id: int, db: Session = Depends(get_db)):
    seller_db = crud.get_seller_by_id(db, seller_id)
    if not seller_db:
        raise HTTPException(status_code=404, detail="Seller not found")
    crud.delete_seller(db, seller_db)
    return
