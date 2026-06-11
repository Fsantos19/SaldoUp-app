from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

from app.core.dependencies import get_current_user

from app.models.user import User

from app.schemas.user import (
    UserCreate,
    UserResponse
)

from app.schemas.auth import (
    LoginRequest,
    TokenResponse
)

from app.repositories.user_repository import (
    UserRepository
)

router = APIRouter()


@router.post(
    "/register",
    response_model=UserResponse
)
def register(
    payload: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = UserRepository.get_by_email(
        db,
        payload.email
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email já cadastrado"
        )

    user = UserRepository.create(
        db=db,
        name=payload.name,
        email=payload.email,
        password_hash=hash_password(
            payload.password
        )
    )

    return user


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    payload: LoginRequest,
    db: Session = Depends(get_db)
):

    user = UserRepository.get_by_email(
        db,
        payload.email
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Credenciais inválidas"
        )

    if not verify_password(
        payload.password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Credenciais inválidas"
        )

    token = create_access_token(
        {
            "sub": str(user.id),
            "email": user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.get(
    "/me",
    response_model=UserResponse
)
def me(
    current_user: User = Depends(get_current_user)
):
    return current_user