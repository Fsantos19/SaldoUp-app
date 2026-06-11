from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user

from app.models.user import User

from app.schemas.category import (
    CategoryCreate,
    CategoryResponse
)

from app.repositories.category_repository import (
    CategoryRepository
)

router = APIRouter()


@router.post(
    "/",
    response_model=CategoryResponse
)
def create_category(
    payload: CategoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return CategoryRepository.create(
        db=db,
        name=payload.name,
        user_id=current_user.id
    )


@router.get(
    "/",
    response_model=list[CategoryResponse]
)
def list_categories(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return CategoryRepository.get_all_by_user(
        db,
        current_user.id
    )