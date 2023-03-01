from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# internal
from app import schemas, models
from app.routers.utils import get_db

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
def create(request: models.Recipe, db: Session = Depends(get_db)):
    new_blog = schemas.Recipe(title=request.title, directions=request.directions)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get("/{recipe_id}/comments")
def get(recipe_id):
    return {"data": f"{recipe_id} Recipe Comments"}
