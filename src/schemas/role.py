from typing import Optional
from pydantic import BaseModel


class RoleResponse(BaseModel):
    name: str
    description: Optional[str]
