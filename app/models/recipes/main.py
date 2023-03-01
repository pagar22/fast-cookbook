from datetime import timedelta
from pydantic import BaseModel


class Recipe(BaseModel):
    title: str
    directions: str
    cooking_time: timedelta
    is_active: bool | None


# {
#   "title": "Fried Chicken",
#   "ingredients": "Chicken",
#   "directions": "Fry in oil",
#   "time": 45
# }
