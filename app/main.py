from fastapi import FastAPI

from app.routers import internal, recipes

app = FastAPI()


app.include_router(internal.router)
app.include_router(recipes.router)
