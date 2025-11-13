from pydantic import BaseModel

class Estado(BaseModel):
    id_estado: int
    nombre: str
    class Config:
        from_attributes = True
