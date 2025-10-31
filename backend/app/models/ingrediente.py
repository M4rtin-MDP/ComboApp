from sqlalchemy import Column, Integer, String, Boolean, Numeric
from sqlalchemy.orm import relationship
from app.db.database import Base

class Ingrediente(Base):
    __tablename__ = "ingrediente"
    id_ingrediente = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    disponible = Column(Boolean, default=True)
    precio = Column(Numeric(10, 2), nullable=False)

    items_ingredientes = relationship("ItemIngrediente", back_populates="ingrediente")
    comidas = relationship("IngrComida", back_populates="ingrediente")
