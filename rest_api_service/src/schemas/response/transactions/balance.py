from _decimal import Decimal
from src.schemas.response.base import BaseResponse


class BalanceChangeResponse(BaseResponse):
    address: str
    balance_change: str

    @classmethod
    def from_wei(cls, address: str, balance_change: float):
        balance_in_eth = Decimal(balance_change) / Decimal(10**18)
        return cls(address=address, balance_change=f"{balance_in_eth:.10f} ETH")
