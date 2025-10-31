from pydantic import BaseModel

class Estado(BaseModel):
    id_estado: int
    nombre: str
    id: int
    class Config:
        from_attributes = True
