from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base

class ComidaBase(Base):
    __tablename__ = "comida_base"
    id_comida = Column(Integer, primary_key=True, index=True)
    id_categoria = Column(String, ForeignKey('categoria.id_categoria'), nullable=False, index=True)
    nombre = Column(String, nullable=False)
    
