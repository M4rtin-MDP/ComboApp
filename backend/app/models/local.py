from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base

class Local(Base):
    __tablename__ = "locals"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    direccion = Column(String)
    latitud = Column(Float)
    longitud = Column(Float)
