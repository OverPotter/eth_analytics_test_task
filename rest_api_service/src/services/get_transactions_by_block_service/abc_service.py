from abc import ABC, abstractmethod

from src.schemas.response.transactions.base import TransactionBaseResponse


class AbstractGetTransactionsByBlockService(ABC):
    @abstractmethod
    async def get_transactions_by_block(
        self, block_to_check: int
    ) -> list[TransactionBaseResponse]: ...
