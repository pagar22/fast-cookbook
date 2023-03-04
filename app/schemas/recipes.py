from datetime import timedelta
from pydantic import BaseModel

# internal
from app.schemas.users import PublicUser


class Recipe(BaseModel):
    title: str
    directions: str
    cooking_time: timedelta | None
    is_active: bool | None
    owner: PublicUser

    class Config:
        orm_mode = True


class RecipeWithoutOwner(BaseModel):
    title: str
    directions: str
    cooking_time: timedelta | None
    is_active: bool | None

    class Config:
        orm_mode = True
