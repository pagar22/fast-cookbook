from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta

# internal
from app import models, schemas
from app.database import get_db
from app.utils import Hash, create_access_token

router = APIRouter(tags=["auth"])


@router.post("/login")
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

    # create JWT token
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
