from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class ItemComida(Base):
    __tablename__ = "items_comida"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_combo = Column(Integer, ForeignKey("combo.id_combo"))
    id_comida = Column(Integer, ForeignKey("comida_base.id_comida"))

    combo = relationship("Combo", back_populates="items_comida")
    comida = relationship("ComidaBase", back_populates="items_comida")
