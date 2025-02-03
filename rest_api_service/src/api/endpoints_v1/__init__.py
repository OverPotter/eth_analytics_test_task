from fastapi import APIRouter
from src.api.endpoints_v1.transactions import router as transactions

router = APIRouter(prefix="/api/v1/eth-analytics-service")

router.include_router(transactions, tags=["transactions"])
