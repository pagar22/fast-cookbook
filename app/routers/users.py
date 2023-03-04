from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

# internal
from app.database import get_db
from app import models, schemas
from app.utils import Hash

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/{user_id}", response_model=schemas.PublicUser)
def get(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} does not exist",
        )
    return user


@router.post("/", response_model=schemas.PublicUser)
def create(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{user_id}/recipes", response_model=List[schemas.RecipeWithoutOwner])
def get(user_id: int, db: Session = Depends(get_db)):
    blogs = db.query(models.Recipe).filter(models.Recipe.owner_id == user_id).all()
    if not blogs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {user_id} does not have any recipes",
        )
    return blogs
