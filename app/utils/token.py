from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import jwt, JWTError
from sqlalchemy.orm import Session

# internal
from app import models, schemas
from app.database import get_db

SECRET_KEY = "e4cf3661ec70bdc532b6049e979581467a42906dd1985db0937d64a91112c40b"
ALGORITHM = "HS256"
OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(data: dict, expires: timedelta | None = timedelta(minutes=30)):
    data_to_encode = data.copy()
    # add expiry timedelta
    data_to_encode.update({"exp": datetime.utcnow() + expires})
    # encode
    encoded_jwt = jwt.encode(data_to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(
    token: str = Depends(OAUTH2_SCHEME), db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="incorrect_credentials"
    )
    try:
        payload = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if not username:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = (
        db.query(models.User)
        .filter(models.User.username == token_data.username)
        .first()
    )
    if not user:
        raise credentials_exception
    return user
