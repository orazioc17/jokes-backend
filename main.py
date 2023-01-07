from fastapi import APIRouter, FastAPI

from routers import jokes
from db import models
from db.database import engine


app = FastAPI()

app.include_router(jokes.router)

models.Base.metadata.create_all(engine)
