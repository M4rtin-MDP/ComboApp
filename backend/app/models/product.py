from sqlalchemy import Column, Integer, String, Float, Text
from app.db.database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    alergenos = Column(Text, nullable=True)
