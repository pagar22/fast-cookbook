from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

# internal
from app import models, schemas
from app.database import get_db
from app.utils import Hash

router = APIRouter(tags=["auth"])


@router.post("/login", response_model=schemas.PublicUser)
def login(request: schemas.LoginOrRegister, db: Session = Depends(get_db)):
    user = (
        db.query(models.User).filter(models.User.username == request.username).first()
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user_not_found"
        )
    if not Hash.verify(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="incorrect_credentials"
        )
    return user
