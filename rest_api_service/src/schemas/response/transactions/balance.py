from src.schemas.response.base import BaseResponse


class BalanceChangeResponse(BaseResponse):
    address: str
    balance_change: float
