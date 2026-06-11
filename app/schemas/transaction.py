from uuid import UUID

from pydantic import BaseModel


class TransactionCreate(BaseModel):
    description: str
    amount: float
    type: str
    category_id: UUID


class TransactionResponse(BaseModel):
    id: UUID
    description: str
    amount: float
    type: str
    category_id: UUID

    class Config:
        from_attributes = True