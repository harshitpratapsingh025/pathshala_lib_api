from typing import List, Optional
from pydantic import BaseModel, EmailStr
from .role import RoleResponse


class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    phone: Optional[str]
    is_active: bool
    roles: List[RoleResponse] = []

    class Config:
        orm_mode = True
