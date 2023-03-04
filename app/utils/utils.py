from passlib.context import CryptContext
from app.database import SessionLocal


class Hash:
    def bcrypt(password: str):
        password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return password_context.hash(password)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
