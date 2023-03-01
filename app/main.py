from fastapi import FastAPI

from app.routers import internal, recipes
from app import schemas
from app.database import engine

app = FastAPI()

schemas.Base.metadata.create_all(bind=engine)


app.include_router(internal.router)
app.include_router(recipes.router)
