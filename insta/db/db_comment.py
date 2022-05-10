from insta.schemas import CommentBase
from sqlalchemy.orm.session import Session
from insta.db.models import DbComment
from datetime import datetime
from fastapi import HTTPException, status


def create(db: Session, request: CommentBase) -> DbComment:
    new_comment = DbComment(
        text=request.text,
        username=request.username,
        post_id=request.post_id,
        timestamp=datetime.utcnow(),
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def get_all(db: Session, post_id: int):
    return db.query(DbComment).filter(DbComment.post_id == post_id).all()
