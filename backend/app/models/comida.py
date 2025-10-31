from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class ComidaBase(Base):
    __tablename__ = "comida_base"
    id_comida = Column(Integer, primary_key=True, index=True)
    id_categoria = Column(Integer, ForeignKey("categoria.id_categoria"))
    nombre = Column(String, nullable=False)

    categoria = relationship("Categoria", back_populates="comidas")
    ingredientes = relationship("IngrComida", back_populates="comida")
    items_comida = relationship("ItemComida", back_populates="comida")
    
