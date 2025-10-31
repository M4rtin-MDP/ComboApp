from sqlalchemy import Column, Integer, ForeignKey, Float, Text
from sqlalchemy.orm import relationship
from app.db.database import Base

class IngrComida(Base):
    __tablename__ = "ingr_comida"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_comida = Column(Integer, ForeignKey("comida_base.id_comida"))
    id_ingrediente = Column(Integer, ForeignKey("ingrediente.id_ingrediente"))

    comida = relationship("ComidaBase", back_populates="ingredientes")
    ingrediente = relationship("Ingrediente", back_populates="comidas")
