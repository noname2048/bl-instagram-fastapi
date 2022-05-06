from insta.schemas import UserBase
from insta.db.models import DbUser
from sqlalchemy.orm import Session
from insta.db.hashing import Hash
from fastapi import status, HTTPException


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_username(db: Session, username: str) -> DbUser:
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with username {username} is not founded",
        )
    return user
