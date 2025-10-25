from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base

class Local(Base):
    __tablename__ = "locals"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    direccion = Column(String, nullable=True)
    latitud = Column(Float, nullable=True)
    longitud = Column(Float, nullable=True)
