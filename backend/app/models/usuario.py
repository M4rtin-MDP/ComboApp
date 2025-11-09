from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base


class Usuario(Base):
    __tablename__ = "usuario"
    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    contrasena = Column(String, nullable=False)
    mail = Column(String, nullable=False, unique=True)
    direccion = Column(String, nullable=True)

    pedidos = relationship("Pedido", back_populates="usuario")
