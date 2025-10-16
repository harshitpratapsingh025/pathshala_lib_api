from fastapi import APIRouter
from src.schemas.auth import (
    UserLoginResponse,
    UserRegisterRequest,
    UserLoginRequest,
    UserRegistrationResponse,
)

router = APIRouter()


@router.post("/", status_code=201)
async def register_user(user: UserRegisterRequest) -> UserRegistrationResponse:
    data = user.model_dump()
    return UserRegistrationResponse(**data, id=1, is_active=True)


@router.post("/token")
async def login_for_access_token(form_data: UserLoginRequest) -> UserLoginResponse:
    return UserLoginResponse(
        access_token="fake-token-12345", refresh_token="fake-refresh-token-12345"
    )
