from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session
from insta.schemas import PostDisplay, PostBase
from insta.db.database import get_db
from insta.db import db_post
from typing import List
import random
import string
import shutil
from insta.schemas import UserAuth
from insta.auth.oauth2 import get_current_user

router = APIRouter(prefix="/post", tags=["post"])

image_url_type = ["absolute", "relative"]


@router.post("", response_model=PostDisplay)
def create(
    request: PostBase,
    db: Session = Depends(get_db),
    current_user: UserAuth = Depends(get_current_user),
):
    if current_user.id != request.creator_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="check creator_id",
        )
    if not request.image_url_type in image_url_type:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABEL_ENTITY,
            detail="Parameter image_url_type can only take values 'absolute' or 'relative'.",
        )

    return db_post.create(db, request)


@router.get("/all", response_model=List[PostDisplay])
def posts(db: Session = Depends(get_db)):
    return db_post.get_all(db)


@router.post("/image")
def upload_image(image: UploadFile = File(...)):
    letters = string.ascii_letters
    rand_str = "".join(random.choice(letters) for i in range(6))
    new = f"_{rand_str}."
    filename = new.join(image.filename.rsplit(".", 1))
    path = f"insta/images/{filename}"

    with open(path, "wb+") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {"filename": path}


@router.get("/delete/{id}")
def delete(
    id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)
):
    return db_post.delete(db, id, current_user.id)
