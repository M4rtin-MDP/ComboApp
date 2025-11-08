from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean, Numeric
from sqlalchemy.orm import relationship
from app.db.database import Base

class Pedido(Base):
    __tablename__ = "pedido"
    id_pedido = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuario.usuario_id"))
    id_restaurante = Column(Integer, ForeignKey("restaurante.id_restaurante"))
    id_estado = Column(Integer, ForeignKey("estado.id_estado"))

    total = Column(Numeric(10, 2), nullable=False)
    fecha = Column(DateTime, nullable=False)
    

    usuario = relationship("Usuario", back_populates="pedidos")
    restaurante = relationship("Restaurante", back_populates="pedidos")
    estado = relationship("Estado", back_populates="pedidos")
