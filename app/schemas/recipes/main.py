from datetime import timedelta
from pydantic import BaseModel


class Recipe(BaseModel):
    title: str
    directions: str
    # cooking_time: timedelta | None
    # is_active: bool | None

    class Config:
        orm_mode = True


# {
#   "title": "Fried Chicken",
#   "ingredients": "Chicken",
#   "directions": "Fry in oil",
#   "time": 45
# }
