from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.exceptions import StoryException
from app.db import models
from app.db.database import engine

from app.router import article, product, user

app = FastAPI()


app.include_router(article.router)
app.include_router(product.router)
app.include_router(user.router)


app.add_middleware(
    CORSMiddleware, allowed_origisn=["*"], allowed_headers=["*"], allowed_methods=["*"]
)


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
