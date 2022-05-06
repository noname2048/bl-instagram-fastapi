from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from insta.schemas import PostDisplay, PostBase
from insta.db.database import get_db
from insta.db import db_post

router = APIRouter(prefix="/post", tags=["post"])

image_url_type = ["absolute", "relative"]


@router.post("", response_model=PostDisplay)
def create(request: PostBase, db: Session = Depends(get_db)):
    if not request.image_url_type in image_url_type:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABEL_ENTITY,
            detail="Parameter image_url_type can only take values 'absolute' or 'relative'.",
        )

    return db_post.create(db, request)
