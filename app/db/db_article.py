from sqlalchemy.orm.session import Session
from schemas import ArticleBase
from db.models import DbArticle


def create_article(request: ArticleBase, db: Session):
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
    # Handle exception
    return article
