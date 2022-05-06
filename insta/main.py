from fastapi import FastAPI
from insta.db import models
from insta.db.database import engine
from insta.routers import user, post, comment
from fastapi.staticfiles import StaticFiles
from insta.auth import authentication
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)
app.include_router(comment.router)
app.include_router(authentication.router)


@app.get("/")
def root():
    return "Hello world!"


origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)

app.mount("/images", StaticFiles(directory="insta/images"), name="images")
