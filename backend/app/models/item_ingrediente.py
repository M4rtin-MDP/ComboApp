from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class ItemIngrediente(Base):
    __tablename__ = "items_ingredientes"
    id_item_ingre = Column(Integer, primary_key=True, index=True)
    id_combo = Column(Integer, ForeignKey("combo.id_combo"))
    id_ingrediente = Column(Integer, ForeignKey("ingrediente.id_ingrediente"))

    combo = relationship("Combo", back_populates="items_ingredientes")
    ingrediente = relationship("Ingrediente", back_populates="items_ingredientes")
