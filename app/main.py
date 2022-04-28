from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from app.exceptions import StoryException
from db import models
from db.database import engine

from router import article, product, user

app = FastAPI()


@app.include_router(article.router)
@app.include_router(product.router)
@app.include_router(user.router)
@app.get("/")
async def index():
    return {"message": "hello world"}


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        content={"detail": exc.name},
    )


models.Base.metadata.create_all(engine)
