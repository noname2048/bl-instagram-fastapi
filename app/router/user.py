from typing import List
from fastapi import APIRouter, Depends
from app.schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db import db_user

router = APIRouter(prefix="/user", tags=["user"])

# Create user
@router.post("/", response_model=UserDisplay)
async def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


# Read all users
@router.get("/", response_model=List[UserDisplay])
async def read_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users()


# Read one user
@router.get("/{:id}", response_model=UserDisplay)
async def read_one_user(id: int, db: Session = Depends(get_db)):
    return db_user.get_user(db, id)


# Update user
@router.post("/{id}/update")
async def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    db_user.update_user(db, id, request)
    return "ok"


# Delete user
@router.get("/delete/{id}")
async def delete_user(id: int, db: Session = Depends(get_db)):
    db_user.delete_user(db, id)
    return "ok"
