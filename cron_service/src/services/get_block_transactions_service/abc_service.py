from abc import ABC, abstractmethod

from src.schemas.response.transactions.base import TransactionBaseResponse


class AbstractGetBlockTransactionsService(ABC):
    @abstractmethod
    async def get_block_transactions(
        self, block_number: int
    ) -> list[TransactionBaseResponse]: ...
