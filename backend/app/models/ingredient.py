from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base

class Ingredient(Base):
    __tablename__ = "ingredients"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False, index=True)
    precio = Column(Float, nullable=False, default=0.0)
