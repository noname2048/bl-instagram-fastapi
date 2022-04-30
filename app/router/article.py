from fastapi import APIRouter, Depends
from app.schemas import ArticleBase, ArticleDisplay
from app.db.database import get_db
from app.db import db_article
from app.schemas import UserBase
from app.auth.oauth2 import get_current_user
from sqlalchemy.orm.session import Session
from app.auth.oauth2 import oauth2_scheme


router = APIRouter(prefix="/article", tags=["article"])


# Create article
@router.post("/", response_model=ArticleDisplay)
async def create_article(
    request: ArticleBase,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    return db_article.create_article(request, db)


# Get specific article
@router.get("/{id}")  # response_model=ArticleDisplay)
async def get_article(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    return {"data": db_article.get_article(id, db), "current_user": current_user}
