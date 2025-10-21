from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.core.database import Base

combo_ingredient = Table(
    "combo_ingredient",
    Base.metadata,
    Column("combo_id", Integer, ForeignKey("combos.id"), primary_key=True),
    Column("ingredient_id", Integer, ForeignKey("ingredients.id"), primary_key=True),
)

class Combo(Base):
    __tablename__ = "combos"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    base_meal = Column(String, nullable=False)
    total_price = Column(Float, nullable=False, default=0.0)
    user_id = Column(Integer, ForeignKey("users.id"))
    ingredients = relationship("Ingredient", secondary=combo_ingredient, backref="combos")
