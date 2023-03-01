from fastapi import APIRouter
from app.models.recipes import Recipe

router = APIRouter(prefix="/recipes", tags=["recipes"])


@router.get("/")
def list(is_active: bool = True, offset: int = 0, limit: int = 10):
    return {
        "data": f"List of {'active' if is_active else 'inactive'} recipes from {offset} to {limit}"
    }


@router.get("/{recipe_id}")
def get(recipe_id: int):
    return {"data": f"Recipe {recipe_id}"}


@router.post("/")
def create(recipe: Recipe):
    return {"data": "New recipe created!"}


@router.get("/{recipe_id}/comments")
def get(recipe_id):
    return {"data": f"{recipe_id} Recipe Comments"}
