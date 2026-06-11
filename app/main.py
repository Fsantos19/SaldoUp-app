from fastapi import FastAPI
from app.api.auth import router as auth_router

from app.api.test_db import router as test_db_router

from app.api.categories import router as categories_router

app = FastAPI(
    title="SaldoUp API"
)

app.include_router(
    test_db_router,
    prefix="/api"
)

app.include_router(
    auth_router,
    prefix="/api/auth",
    tags=["Auth"]
)


@app.get("/")
def home():
    return {
        "message": "SaldoUp API funcionando"
    }
    
app.include_router(
    categories_router,
    prefix="/api/categories",
    tags=["Categories"]
)