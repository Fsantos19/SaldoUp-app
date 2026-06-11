from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer

from jose import JWTError
from jose import jwt

from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.database import get_db

from app.models.user import User


security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):

    token = credentials.credentials

    print("\n===== DEBUG JWT =====")
    print("TOKEN:", token)
    print("SECRET_KEY:", settings.SECRET_KEY)
    print("ALGORITHM:", settings.ALGORITHM)

    try:

        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        print("PAYLOAD:", payload)

        user_id = payload.get("sub")

        if not user_id:
            raise HTTPException(
                status_code=401,
                detail="Token inválido"
            )

    except JWTError as e:

        print("ERRO JWT:", str(e))

        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Usuário não encontrado"
        )

    return user