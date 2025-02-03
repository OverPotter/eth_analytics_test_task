from src.database.repositories.transaction_repository import (
    TransactionRepository,
)
from src.schemas.response.transactions.base import TransactionBaseResponse
from src.services.save_transactions_service.abc_service import (
    AbstractSaveTransactionsService,
)


class RepositorySaveTransactionsService(AbstractSaveTransactionsService):
    def __init__(
        self,
        transaction_repository: TransactionRepository,
    ):
        self._transaction_repository = transaction_repository

    async def save_transactions(
        self, transactions: list[TransactionBaseResponse]
    ) -> None:
        await self._transaction_repository.create_transactions(
            transactions=transactions
        )
