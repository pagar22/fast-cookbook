from fastapi import FastAPI

from app.routers import internal, recipes, users
from app import models
from app.database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


app.include_router(internal.router)
app.include_router(recipes.router)
app.include_router(users.router)
