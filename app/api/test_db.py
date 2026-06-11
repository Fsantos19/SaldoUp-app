from fastapi import APIRouter
from sqlalchemy import text

from app.core.database import SessionLocal

router = APIRouter()


@router.get("/test-db")
def test_db():

    db = SessionLocal()

    try:
        result = db.execute(
            text("SELECT version();")
        )

        version = result.scalar()

        return {
            "status": "connected",
            "database": version
        }

    finally:
        db.close()