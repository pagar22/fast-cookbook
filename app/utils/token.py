from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "e4cf3661ec70bdc532b6049e979581467a42906dd1985db0937d64a91112c40b"
ALGORITHM = "HS256"


def create_access_token(data: dict, expires: timedelta | None = timedelta(minutes=30)):
    data_to_encode = data.copy()
    # add expiry timedelta
    data_to_encode.update({"exp": datetime.utcnow() + expires})
    # encode
    encoded_jwt = jwt.encode(data_to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
