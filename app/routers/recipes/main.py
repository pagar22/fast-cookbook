from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

# internal
from app import schemas, models
from app.routers.utils import get_db

router = APIRouter(prefix="/recipes", tags=["recipes"])


@router.get("/")
def list(
    db: Session = Depends(get_db),
):
    recipes = db.query(schemas.Recipe).all()
    return recipes


@router.get("/{recipe_id}")
def get(recipe_id: int, response: Response, db: Session = Depends(get_db)):
    recipe = db.query(schemas.Recipe).filter(schemas.Recipe.id == recipe_id).first()
    if not recipe:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Detail": f"Recipe with id {recipe_id} does not exist"}
    return recipe


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: models.Recipe, db: Session = Depends(get_db)):
    new_blog = schemas.Recipe(title=request.title, directions=request.directions)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {}


@router.get("/{recipe_id}/comments")
def get(recipe_id):
    return {"data": f"{recipe_id} Recipe Comments"}
