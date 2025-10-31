from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PedidoBase(BaseModel):
    id_usuario: str
    id_restaurante: int
    id_estado: int
    id_combo: int
    fecha: datetime
    total: float

class PedidoCreate(PedidoBase):
    pass

class Pedido(PedidoBase):
    id_pedido: int
    class Config:
        from_attributes = True
