from typing import Annotated, Optional
from pydantic import BaseModel, EmailStr, Field, field_validator

Phone = Annotated[str, Field(example="+919876543210", description="E.164")]
FullName = Annotated[str, Field(min_length=3, max_length=50, example="John Doe")]


class UserRegisterRequest(BaseModel):
    full_name: FullName
    email: EmailStr
    password: str
    phone: Phone

    @field_validator("phone", mode="before")
    @classmethod
    def validate_phone(cls, value):
        if (
            not value.startswith("+")
            or not value[1:].isdigit()
            or len(value) < 10
            or len(value) > 15
        ):
            raise ValueError("Phone number must be in E.164 format")
        return value

    @field_validator("password", mode="before")
    @classmethod
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return value


class UserLoginRequest(BaseModel):
    username: str
    password: str


class UserLoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    refresh_token: Optional[str] = None


class UserRegistrationResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: FullName
    phone: Phone
    is_active: bool
