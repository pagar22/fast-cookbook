from app.database import Base
from sqlalchemy import Column, Integer, String


class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    directions = Column(String)
