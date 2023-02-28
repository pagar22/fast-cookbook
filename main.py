from fastapi import FastAPI

router = FastAPI()


@router.get("/ping")
def ping():
    return {"data": "ping!"}


@router.get("/recipes")
def list(offset: int = 0, limit: int = 10):
    return {"data": f"List of recipes from {offset} to {limit}"}


@router.get("/recipe/{recipe_id}")
def get(recipe_id: int):
    return {"data": f"Recipe {recipe_id}"}


@router.get("/recipe/{recipe_id}/comments")
def get(recipe_id):
    return {"data": f"{recipe_id} Recipe Comments"}
