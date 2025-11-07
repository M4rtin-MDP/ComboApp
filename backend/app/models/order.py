from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.db.database import Base

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    combo_id = Column(Integer, ForeignKey("combos.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    local_id = Column(Integer, ForeignKey("locals.id"))
    estado = Column(String, default="pendiente")
    total = Column(Float, nullable=True)
