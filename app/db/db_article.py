from sqlalchemy.orm.session import Session
from app.exceptions import StoryException
from schemas import ArticleBase
from db.models import DbArticle
from fastapi import HTTPException, status


def create_article(request: ArticleBase, db: Session):
    if request.content.startswith("Once upon a time"):
        raise StoryException("No stories pleas")

    new_article = DbArticle(
        title=request.title,
        content=request.content,
        published=request.published,
        user_id=request.creator_id,
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def get_article(id: int, db: Session):
    article = db.query(DbArticle).filter(DbArticle.id == id).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article with id {id} not found",
        )
    return article
