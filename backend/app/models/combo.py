from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Combo(Base):
    __tablename__ = "combo"
    id_combo = Column(Integer, primary_key=True, index=True)
    id_pedido = Column(Integer, ForeignKey("pedido.id_pedido"))

    pedido = relationship("Pedido", back_populates="combo")
    items_comida = relationship("ItemComida", back_populates="combo")
    items_ingredientes = relationship("ItemIngrediente", back_populates="combo")