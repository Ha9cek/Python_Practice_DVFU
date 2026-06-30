from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db import crud
from app.db.models import Book
from app import schemas

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/", response_model=List[schemas.BookResponse])
def list_books(category_id: Optional[int] = None, db: Session = Depends(get_db)):
    if category_id is not None:
        return db.query(Book).filter(Book.category_id == category_id).all()
    return crud.get_books(db)


@router.get("/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.post("/", response_model=schemas.BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(data: schemas.BookCreate, db: Session = Depends(get_db)):
    if not crud.get_category(db, data.category_id):
        raise HTTPException(status_code=404, detail="Category not found")
    return crud.create_book(db, data.title, data.description, data.price, data.url, data.category_id)


@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, data: schemas.BookCreate, db: Session = Depends(get_db)):
    if not crud.get_category(db, data.category_id):
        raise HTTPException(status_code=404, detail="Category not found")
    book = crud.update_book(
        db, book_id,
        title=data.title,
        description=data.description,
        price=data.price,
        url=data.url,
        category_id=data.category_id,
    )
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.delete_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return None