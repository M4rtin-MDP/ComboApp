from pydantic import BaseModel
from typing import Optional

class OrderCreate(BaseModel):
    combo_id: int
    user_id: int
    local_id: int

class OrderRead(BaseModel):
    id: int
    combo_id: int
    user_id: int
    local_id: int
    estado: Optional[str] = None
    total: Optional[float] = None

    class Config:
        from_attributes = True
