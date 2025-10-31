from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base

class Estado(Base):
    __tablename__ = "estado"
    id_estado = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)

    pedidos = relationship("Pedido", back_populates="estado")
