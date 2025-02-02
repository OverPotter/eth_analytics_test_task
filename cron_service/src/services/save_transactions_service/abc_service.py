from abc import ABC, abstractmethod

from src.schemas.response.transactions.base import TransactionBaseResponse


class AbstractSaveTransactionsService(ABC):
    @abstractmethod
    async def save_transactions(
        self, transactions: list[TransactionBaseResponse]
    ) -> None: ...
