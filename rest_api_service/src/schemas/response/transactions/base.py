from src.schemas.response.base import BaseResponse


class TransactionBaseResponse(BaseResponse):
    block_number: int
    tx_from: str
    tx_to: str | None = None
    value: int
