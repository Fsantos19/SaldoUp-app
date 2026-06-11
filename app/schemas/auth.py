from pydantic import BaseModel, EmailStr


from app.core.security import (
    verify_password,
    create_access_token
)

class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str