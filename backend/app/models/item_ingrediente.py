from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class ItemIngrediente(Base):
    __tablename__ = "items_ingredientes"
    item_ingrediente = Column(Integer, primary_key=True, index=True)
    item_comida = Column(Integer, ForeignKey("items_comida.item_comida"))
    id_ingrediente = Column(Integer, ForeignKey("ingrediente.id_ingrediente"))

    items_comida = relationship("ItemComida", back_populates="items_ingredientes")
    ingrediente = relationship("Ingrediente", back_populates="items_ingredientes")
