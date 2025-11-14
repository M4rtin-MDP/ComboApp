from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PedidoBase(BaseModel):
    id_usuario: int
    id_restaurante: int
    id_estado: int
    fecha: datetime
    total: float

class PedidoCreate(PedidoBase):
    id_usuario: int
    id_restaurante: int
    id_estado: int
    fecha: datetime
    total: float

class Pedido(PedidoBase):
    id_pedido: int
    class Config:
        from_attributes = True
        
