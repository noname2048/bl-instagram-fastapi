from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from insta.db.database import get_db
from insta.db import db_comment
from insta.schemas import CommentBase
from insta.auth.oauth2 import get_current_user


router = APIRouter(prefix="/comment", tags=["comments"])


@router.get("/all/{post_id}")
def get_all(post_id: int, db: Session = Depends(get_db)):
    return db_comment.get_all(db, post_id)


@router.post("")
def create(
    request: CommentBase,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return db_comment.create(db, request)
