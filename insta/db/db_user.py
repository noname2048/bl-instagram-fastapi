from insta.schemas import UserBase
from insta.db.models import DbUser
from sqlalchemy.orm import Session
from insta.db.hashing import Hash


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
