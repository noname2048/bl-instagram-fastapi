from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.exceptions import StoryException
from app.db import models
from app.db.database import engine

from app.router import article, product, user, file
from app.templates import templates
from app.auth import authentication

import time

app = FastAPI()


app.include_router(templates.router)
app.include_router(authentication.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(user.router)
app.include_router(file.router)

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_headers=["*"], allow_methods=["*"]
)
app.mount("/files", StaticFiles(directory="./app/files"), name="files")
app.mount(
    "/templates/static", StaticFiles(directory="./app/templates/static"), name="static"
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


@app.middleware("http")
async def add_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    response.headers["duration"] = str(duration)
    return response
