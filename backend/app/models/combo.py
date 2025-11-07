from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.db.database import Base

combo_ingredient = Table(
    "combo_ingredient",
    Base.metadata,
    Column("combo_id", Integer, ForeignKey("combos.id"), primary_key=True),
    Column("product_id", Integer, ForeignKey("products.id"), primary_key=True),
)

class Combo(Base):
    __tablename__ = "combos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=True)
    base_id = Column(Integer, ForeignKey("products.id"))
    bebida_id = Column(Integer, ForeignKey("products.id"), nullable=True)
    acompanamiento_id = Column(Integer, ForeignKey("products.id"), nullable=True)
    total = Column(Float, nullable=False, default=0.0)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    base = relationship("Product", foreign_keys=[base_id])
    bebida = relationship("Product", foreign_keys=[bebida_id])
    acompanamiento = relationship("Product", foreign_keys=[acompanamiento_id])
    ingredients = relationship("Product", secondary=combo_ingredient, backref="combos")
