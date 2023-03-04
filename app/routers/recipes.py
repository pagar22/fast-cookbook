from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

# internal
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/recipes", tags=["recipes"])


@router.get("/", response_model=List[schemas.Recipe])
def get_all(db: Session = Depends(get_db)):
    recipes = db.query(models.Recipe).all()
    return recipes


@router.get("/{recipe_id}", response_model=schemas.Recipe)
def get(recipe_id: int, db: Session = Depends(get_db)):
    recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Recipe with id {recipe_id} does not exist",
        )
    return recipe


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.RecipeWithoutOwner, db: Session = Depends(get_db)):
    new_blog = models.Recipe(
        title=request.title, directions=request.directions, owner_id=1
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {}


@router.patch("/{recipe_id}", status_code=status.HTTP_202_ACCEPTED)
def update(
    recipe_id, request: schemas.RecipeWithoutOwner, db: Session = Depends(get_db)
):
    recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    if not recipe.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Recipe with id {recipe_id} does not exist",
        )

    # TODO replace with request without destructuring
    recipe.update({"title": request.title, "directions": request.directions})
    db.commit()
    return {}


@router.delete("/{recipe_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(recipe_id: int, db: Session = Depends(get_db)):
    recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    if not recipe.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Recipe with id {recipe_id} does not exist",
        )
    recipe.delete(synchronize_session=False)
    db.commit()
    return {}


@router.get("/{recipe_id}/comments")
def get(recipe_id):
    return {"data": f"{recipe_id} Recipe Comments"}
