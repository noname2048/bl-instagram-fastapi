from fastapi import APIRouter, Depends
from schemas import ArticleBase, ArticleDisplay
from db.database import get_db
from db import db_article
from sqlalchemy.orm.session import Session

router = APIRouter(prefix="/article", tags=["article"])


# Create article
@router.post("/", response_model=ArticleDisplay)
async def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(request, db)


# Get specific article
@router.get("/{id}", response_model=ArticleDisplay)
async def get_article(id: int, db: Session = Depends(get_db)):
    return db_article.get_article(int, db)
