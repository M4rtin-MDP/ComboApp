from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from app.db.database import Base

class Restaurante(Base):
    __tablename__ = "restaurante"
    id_restaurante = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    latitud = Column(Float, nullable=True)
    longitud = Column(Float, nullable=True)
    disponible = Column(Boolean, default=True)

    pedidos = relationship("Pedido", back_populates="restaurante")
