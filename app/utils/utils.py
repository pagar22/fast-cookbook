from passlib.context import CryptContext
from app.database import SessionLocal

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    def bcrypt(password: str):
        return password_context.hash(password)

    def verify(request_pass, hashed_pass):
        return password_context.verify(request_pass, hashed_pass)
