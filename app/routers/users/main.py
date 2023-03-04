from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# internal
from app.routers.utils import get_db
from app import models, schemas

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def get(user_id, db: Session = Depends(get_db)):
    pass


@router.post("/")
def create(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(
        username=request.username, email=request.email, password=request.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {}
