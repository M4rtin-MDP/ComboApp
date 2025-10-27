from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    nombre: str
    email: Optional[EmailStr] = None

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    nombre: str
    email: EmailStr
    class Config:
        from_attributes = True
