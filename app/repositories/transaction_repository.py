from sqlalchemy.orm import Session

from app.models.transaction import Transaction


class TransactionRepository:

    @staticmethod
    def create(
        db: Session,
        description: str,
        amount: float,
        type: str,
        user_id,
        category_id
    ):

        transaction = Transaction(
            description=description,
            amount=amount,
            type=type,
            user_id=user_id,
            category_id=category_id
        )

        db.add(transaction)
        db.commit()
        db.refresh(transaction)

        return transaction

    @staticmethod
    def get_all(
        db: Session,
        user_id
    ):

        return (
            db.query(Transaction)
            .filter(Transaction.user_id == user_id)
            .all()
        )