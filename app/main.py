from fastapi import FastAPI

from app.routers import internal, recipes
from app.schemas.recipes import Base
from app.database import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)


app.include_router(internal.router)
app.include_router(recipes.router)
