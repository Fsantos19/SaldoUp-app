from sqlalchemy.orm import Session

from app.models.category import Category


class CategoryRepository:

    @staticmethod
    def create(
        db: Session,
        name: str,
        user_id
    ):

        category = Category(
            name=name,
            user_id=user_id
        )

        db.add(category)
        db.commit()
        db.refresh(category)

        return category

    @staticmethod
    def get_all_by_user(
        db: Session,
        user_id
    ):

        return (
            db.query(Category)
            .filter(Category.user_id == user_id)
            .order_by(Category.name)
            .all()
        )