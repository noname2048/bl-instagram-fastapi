from fastapi import FastAPI
from insta.db import models
from insta.db.database import engine
from insta.routers import user, post

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)


@app.get("/")
def root():
    return "Hello world!"


models.Base.metadata.create_all(engine)
